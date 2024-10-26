import requests
from bs4 import BeautifulSoup
import json
from rich.console import Console
from rich.panel import Panel
import csv
from modules.scraper import scrape_site_with_pagination, scrape_item
from modules.gui import display_menu_prompt, print_line, print_input
from modules.display import select_subsystem, display_subtopics, select_subsystem_topic, get_url_from_subsystem, select_component
from modules.config import SUBSUBSYSTEMS_URLS

console = Console()

menu_items = [
    ("1.", "SUBSYSTEM ITEMS"),
    ("2.", "ITEM DETAILS"),
    ("3.", "EXIT"),
]

download_items = [
    ("1.", "JSON"),
    ("2.", "CSV"),
    ("3.", "TXT"),
]

# Function to save data to a JSON file
def save_to_json(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

def save_to_txt(data, filename):
    data = json.loads(json.dumps(data))
    lines = []
    for item in data:
        if len(data) > 1:
            lines.append("=" * 70)
        for k, v in item.items():
            if k == 'details':
                for key, value in v.items():
                    lines.append(f"{key.upper()} {value}")
            else:
                lines.append(f"{k.upper()} {v}")

    try:
        with open(filename, 'w') as f:
            for line in lines:
                f.write(str(line) + "\n")
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")


# Functions to Download Item Data
def save_to_txt_item(data, filename):
    data = json.loads(json.dumps(data))
    lines = []
    for item in items:
        lines.append("=" * 70)
        for k, v in item.items():
            if k == 'product_details' or  k == 'general_parameters':
                for key, value in v.items():
                    lines.append(f"{key.upper()} {value}")
            else:
                lines.append(f"{k.upper()} {v}")

    try:
        with open(filename, 'w') as f:
            for line in lines:
                f.write(str(line) + "\n")
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving data to file: {e}")

# Helper Functions for `save_to_csv`

# Recursive function to flatten JSON keys
def flatten_json_keys(nested_dict, parent_key=''):
    keys = []
    for key, value in nested_dict.items():
        if key[len(key) - 1] == ":":
            full_key = key[:len(key) - 1]
        else:
            full_key = key

        if full_key[0].islower():
            full_key = full_key.capitalize()

        if isinstance(value, dict):
            keys.extend(flatten_json_keys(value, full_key))
        else:
            keys.append(full_key)
    return keys

# Function to gather all unique keys for CSV header
def gather_all_keys(json_data):
    all_keys = set()  # Use a set to avoid duplicate keys
    for item in json_data:
        item_keys = flatten_json_keys(item)
        all_keys.update(item_keys)
    return sorted(all_keys)

def gather_all_data(data, csv_header):
    output = []
    for item in data:
        mapping = {header.strip(): "" for header in csv_header}
        flatten_json = lambda d: {**{k: v for k, v in d.items() if k != 'details'}, **{k: v for k, v in d['details'].items()}}
        item = flatten_json(item)
        for key, value in item.items():
            if key[len(key) - 1] == ":":
                full_key = key[:len(key) - 1]
            else:
                full_key = key

            if full_key[0].islower():
                full_key = full_key.capitalize()

            if full_key in mapping:
                mapping[full_key] = value
            elif full_key in item.get('details', {}):
                mapping[full_key] = item['details'][source_key]
            else:
                mapping[full_key] = ""
        output.append(mapping)
    return output

def gather_all_data_item(data, csv_header):
    output = []
    for item in data:
        mapping = {header.strip(): "" for header in csv_header}
        flatten_json = lambda d: {
        **{k: v for k, v in d.items() if k not in ['product_details', 'general_parameters']},
        **{k: v for k, v in d.get('product_details', {}).items()},
        **{k: v for k, v in d.get('general_parameters', {}).items()
        }
}
        item = flatten_json(item)
        for key, value in item.items():
            if key[len(key) - 1] == ":":
                full_key = key[:len(key) - 1]
            else:
                full_key = key

            if full_key[0].islower():
                full_key = full_key.capitalize()

            if full_key in mapping:
                mapping[full_key] = value
            elif full_key in item.get('details', {}):
                mapping[full_key] = item['details'][source_key]
            else:
                mapping[full_key] = ""
        output.append(mapping)
    return output

def save_to_csv(data, filename):
    data = json.loads(json.dumps(data))
    csv_headers = gather_all_keys(data)
    data = gather_all_data(data, csv_headers)

    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_headers)
        for item in data:
            writer.writerow(item.values())
    print(f"Data successfully saved to {filename}")

def save_to_csv_item(data, filename):
    data = json.loads(json.dumps(data))
    csv_headers = gather_all_keys(data)
    data = gather_all_data_item(data, csv_headers)

    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(csv_headers)
        for item in data:
            writer.writerow(item.values())
    print(f"Data successfully saved to {filename}")

def display_download_prompt():
    print_line("\n 💾 DOWNLOAD OPTIONS", "bold")
    choice = display_menu_prompt(menu_items, "bright_magenta", False)

    if choice == "1":
        download_subsystem()
    elif choice == "2":
        download_item_specific_page()
    elif choice == "3":
        exit_program()
    else:
        print_line("Invalid option. Please choose a number between 1 and 5.", "bold red")

def display_download_options(data):
    print_line("\n 📁 FILE FORMAT", "bold")

    choice = display_menu_prompt(download_items, "bright_magenta", False)

    file_name = print_input("Enter file name: ", "blue")

    if choice == "1":
        save_to_json(data["items"], file_name + ".json")
    elif choice == "2":
        save_to_csv(data["items"], file_name + ".csv")
    elif choice == "3":
        save_to_txt(data["items"], file_name + ".txt")
    else:
        print_line("Invalid option. Please choose a number between 1 and 5.", "bold red")

def display_download_options_item(data):
    print_line("\n 📁 FILE FORMAT", "bold")

    choice = display_menu_prompt(download_items, "bright_magenta", False)

    file_name = print_input("Enter file name: ", "blue")

    if choice == "1":
        save_to_json([data], file_name + ".json")
    elif choice == "2":
        save_to_csv_item(data, file_name + ".csv")
    elif choice == "3":
        save_to_txt(data, file_name + ".txt")
    else:
        print_line("Invalid option. Please choose a number between 1 and 5.", "bold red")

def download_subsystem():
    input = select_subsystem()
    subtopic = select_subsystem_topic(input)
    url = get_url_from_subsystem(subtopic)
    result = scrape_site_with_pagination(url)
    display_download_options(result)

def download_item_specific_page():
    input = select_subsystem()
    subtopic = select_subsystem_topic(input)
    url = get_url_from_subsystem(subtopic)
    result = scrape_site_with_pagination(url)
    data = json.loads(json.dumps(result))["items"]
    component = select_component(input, data)
    component_url = component["link"]
    component_data = scrape_item(component_url)
    display_download_options_item(component_data)

def exit_program():
    print_line("Exiting the program...", "bold red")
    exit()