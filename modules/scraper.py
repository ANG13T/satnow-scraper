import requests
from bs4 import BeautifulSoup

def get_total_pages(url):
    """Returns a number denoting the total number of pages by analyzing the internal HTML."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find pagination element and extract all page numbers
        pagination = soup.select_one('ul#pagingDiv')
        if pagination:
            page_links = pagination.select('li.page-item > a.page-link')

            # Filter valid numeric page links
            page_numbers = []
            for link in page_links:
                try:
                    page_number = int(link.get_text(strip=True))
                    page_numbers.append(page_number)
                except ValueError:
                    # Skip over "Previous" and "Next"
                    continue

            if page_numbers:
                return max(page_numbers)  # Return the highest page number found

        return 1  # Default to 1 page if no pagination found

    except requests.RequestException as e:
        print(f"Error fetching pagination data from {url}: {e}")
        return 1

def scrape_site_with_pagination(url):
    """Gets the total number of pages and then scrapes each page for items."""
    total_pages = get_total_pages(url)
    all_items = []


    for page_number in range(1, total_pages + 1):
        page_url = f"{url}/filters?page={page_number}"
        page_items = scrape_page(page_url)
        all_items.extend(page_items)

    return {'items': all_items}

def scrape_page(url):
    """Scrapes data from a single page and returns the items"""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        items = []

        # Find all elements with the 'col-xl-8 col-lg-8 col-md-7 col-sm-8 centerLeft' class
        for item in soup.find_all(class_='col-xl-8 col-lg-8 col-md-7 col-sm-8 centerLeft'):
            item_data = {}

            # TITLE: h3.prod-title > a (get the text inside the title link)
            title_tag = item.select_one('h3.prod-title > a')
            if title_tag:
                item_data['title'] = title_tag.get_text(strip=True)

                # LINK: h3.prod-title > a.href (get the href attribute of the link)
                item_data['link'] = title_tag['href']

            # ORGANIZATION: .moreinfo > a.cur (get the organization link's text)
            org_tag = item.select_one('.moreinfo > a.cur')
            if org_tag:
                item_data['organization'] = org_tag.get_text(strip=True)

            # SKU: .descriptiontext > TEXT (get text inside descriptiontext class)
            sku_tag = item.select_one('.descriptiontext')
            if sku_tag:
                item_data['sku'] = sku_tag.get_text(strip=True)[4:]

            # DETAILS: .specs > .data-row > (.attribute + .value) (loop over data-row items to extract attribute-value pairs)
            details = {}
            spec_rows = item.select('.specs > .data-row')
            for row in spec_rows:
                attribute = row.select_one('.attribute')
                value = row.select_one('.value')
                if attribute and value:
                    details[attribute.get_text(strip=True)] = value.get_text(strip=True)

            if details:
                item_data['details'] = details

            items.append(item_data)

        return items

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

def scrape_item(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        items = []

        # Find all elements with the 'specs' class
        for item in soup.select('.specs'):
            item_data = {}
            product_details = {}
            general_parameters = {}

            product_details_section = item.select_one('.spec-container:nth-of-type(1) .spec-values ul')
            if product_details_section:
                for detail in product_details_section.find_all('li'):
                    field = detail.select_one('.field')
                    value = detail.select_one('.value')
                    if field and value:
                        product_details[field.get_text(strip=True)] = value.get_text(strip=True)

            general_parameters_section = item.select_one('.spec-container:nth-of-type(2) .spec-values ul')
            if general_parameters_section:
                for param in general_parameters_section.find_all('li'):
                    field = param.select_one('.field')
                    value = param.select_one('.value')
                    if field and value:
                        general_parameters[field.get_text(strip=True)] = value.get_text(strip=True)

            technical_document_datasheet = None
            technical_docs_section = item.select_one('.spec-container.ds-action-container .spec-values ul')
            if technical_docs_section:
                datasheet_link = technical_docs_section.select_one('a')
                if datasheet_link and 'href' in datasheet_link.attrs:
                    technical_document_datasheet = datasheet_link['href']

            manufacturer_website_link = None
            manufacturer_link_section = item.select_one(".manuwebsitelink-similar")
            if manufacturer_link_section:
                manufacturer_link = manufacturer_link_section.select_one('a')  # Adjust selector if necessary
                if manufacturer_link and 'href' in manufacturer_link.attrs:
                    manufacturer_website_link = manufacturer_link['href']

            # Compile data into item_data dictionary
            item_data['product_details'] = product_details
            item_data['general_parameters'] = general_parameters
            item_data['technical_document_datasheet'] = technical_document_datasheet
            item_data['manufacturer_website_link'] = manufacturer_website_link  # Add the manufacturer website link
            item_data['url'] = url
            items.append(item_data)

        return items

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []
