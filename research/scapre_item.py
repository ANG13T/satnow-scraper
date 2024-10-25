import requests
from bs4 import BeautifulSoup
import json

# Function to scrape and structure data from a single page
def scrape_page(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        items = []

        # Find all elements with the 'specs' class
        for item in soup.select('.specs'):
            item_data = {}
            product_details = {}
            general_parameters = {}

            # Extract Product Details
            product_details_section = item.select_one('.spec-container:nth-of-type(1) .spec-values ul')
            if product_details_section:
                for detail in product_details_section.find_all('li'):
                    field = detail.select_one('.field')
                    value = detail.select_one('.value')
                    if field and value:
                        product_details[field.get_text(strip=True)] = value.get_text(strip=True)

            # Extract General Parameters
            general_parameters_section = item.select_one('.spec-container:nth-of-type(2) .spec-values ul')
            if general_parameters_section:
                for param in general_parameters_section.find_all('li'):
                    field = param.select_one('.field')
                    value = param.select_one('.value')
                    if field and value:
                        general_parameters[field.get_text(strip=True)] = value.get_text(strip=True)

            # Extract Technical Document URL
            technical_document_datasheet = None
            technical_docs_section = item.select_one('.spec-container.ds-action-container .spec-values ul')
            if technical_docs_section:
                datasheet_link = technical_docs_section.select_one('a')
                if datasheet_link and 'href' in datasheet_link.attrs:
                    technical_document_datasheet = datasheet_link['href']

            # Extract Manufacturer Website Link
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
                
                # Print the Product Details
                f.write("PRODUCT DETAILS:\n")
                for key, value in item['product_details'].items():
                    f.write(f"{key}: {value}\n")
                
                f.write("\nGENERAL PARAMETERS:\n")
                for key, value in item['general_parameters'].items():
                    f.write(f"{key}: {value}\n")
                
                f.write(f"Manufacturer Website Link: {item.get('manufacturer_website_link', 'N/A')}\n")  # Added manufacturer link
                f.write("=" * 62)
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

# Function to print data in a readable format
def print_data(data):
    for item in data['items']:
        print("\nItem:")
        print("  PRODUCT DETAILS:")
        for key, value in item['product_details'].items():
            print(f"    {key}: {value}")
        print("  GENERAL PARAMETERS:")
        for key, value in item['general_parameters'].items():
            print(f"    {key}: {value}")
        print(f"  Manufacturer Website Link: {item.get('manufacturer_website_link', 'N/A')}")  # Added manufacturer link

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

