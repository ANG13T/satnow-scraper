import requests
from bs4 import BeautifulSoup
import json

# Function to scrape and structure data
def scrape_site(url):
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
                item_data['sku'] = sku_tag.get_text(strip=True)

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

        return {'items': items}

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return {'error': 'Failed to retrieve data'}

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    result = scrape_site(url)
    
    # Print JSON result
    print(json.dumps(result, indent=4))

