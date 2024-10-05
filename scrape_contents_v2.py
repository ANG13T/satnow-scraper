import requests
from bs4 import BeautifulSoup
import json

# Function to scrape and structure data from a single page
def scrape_page(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        items = []

        # Find all elements with the 'col-xl-8 col-lg-8 col-md-7 col-sm-8 centerLeft' class
        for item in soup.find_all(class_='product-box'):
            item_data = {}

            # TITLE: h3.prod-title > a (get the text inside the title link)
            title_tag = item.select_one('h3.prod-title > a')
            if title_tag:
                item_data['title'] = title_tag.get_text(strip=True)

                # LINK: h3.prod-title > a.href (get the href attribute of the link)

            # IMAGE: a.imagelink (get the image link)
            img_tag = item.select_one('img.componentImg')
            if img_tag:
                item_data['image'] = img_tag['src']  # Assuming the image URL is in the 'href' attribute
            
            # LINK: a.imagelink
            link_tag = item.select_one('a.imagelink')

            if link_tag:
                item_data['link'] = link_tag['href']

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
                    details[attribute.get_text(strip=True)[:-1]] = value.get_text(strip=True)

            if details:
                item_data['details'] = details

            items.append(item_data)

        return items

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []

# Function to get the total number of pages from pagination
def get_total_pages(url):
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

# Main function to scrape all pages
def scrape_site_with_pagination(url):
    total_pages = get_total_pages(url)
    all_items = []

    print(f"Total pages found: {total_pages}")
    
    for page_number in range(1, total_pages + 1):
        page_url = f"{url}?page={page_number}"
        print(f"Scraping page {page_number}: {page_url}")
        page_items = scrape_page(page_url)
        all_items.extend(page_items)

    return {'items': all_items}

# Function to save data to a JSON file
def save_to_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

# Function to save data to a structured TXT file
def save_to_txt(data, filename):
    try:
        with open(filename, 'w') as f:
            first_entry = True
            for item in data['items']:
                if first_entry:
                    f.write("=" * 62 + "\n")
                    first_entry = False
                else:
                    f.write("\n")
                
                f.write(f"NAME: {item.get('title', 'N/A')}\n")
                f.write(f"ORGANIZATION: {item.get('organization', 'N/A')}\n")
                f.write(f"SKU: {item.get('sku', 'N/A')}\n")
                
                if 'image' in item:
                    f.write(f"IMAGE: {item.get('image', 'N/A')}\n")
                
                if 'details' in item:
                    for key, value in item['details'].items():
                        f.write(f"{key.upper()}: {value}\n")
                
                f.write("=" * 62)
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

# Function to print data in a readable format
def print_data(data):
    for item in data['items']:
        print("\nItem:")
        if 'title' in item:
            print(f"  Title: {item['title']}")
        if 'link' in item:
            print(f"  Link: {item['link']}")
        if 'image' in item:
            print(f"  Image: {item['image']}")
        if 'organization' in item:
            print(f"  Organization: {item['organization']}")
        if 'sku' in item:
            print(f"  SKU: {item['sku']}")
        if 'details' in item:
            print("  Details:")
            for key, value in item['details'].items():
                print(f"    {key}: {value}")

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    result = scrape_site_with_pagination(url)

    # Print data to console
    print_data(result)
    
    # Save the JSON result to a file
    json_filename = "scraped_data.json"
    save_to_json(result, json_filename)

    # Save the structured output to a TXT file
    txt_filename = "scraped_data.txt"
    save_to_txt(result, txt_filename)

