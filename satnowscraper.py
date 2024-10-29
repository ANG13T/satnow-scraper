"""
 SatNow Web Scraper Utility
 OSINT web scraper for SatNow to extract detailed satellite component and subsystem specs for in-depth reconnaissance.

 USAGE: python3 satnowscraper.py

 Written by G4LXY @ 10/25/2024 [19:13:58 PT / 02:14:35 TAI] - Earth (Sol III)
 G4LXY 🙮 M4R$
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from modules.display import select_subsystem, display_subtopics, select_subsystem_topic, get_url_from_subsystem, select_component
from modules.download import display_download_prompt, flatten_json_keys, gather_all_keys, gather_all_data
from modules.scraper import scrape_site_with_pagination, scrape_item
from modules.gui import print_styled_items, print_styled_component, print_styled_items_with_keyword_highlights, print_styled_component
import json

console = Console()

menu_items = [
    ("1.", "SCAN SUBSYSTEM CATALOG"),
    ("2.", "SCAN COMPONENT"),
    ("3.", "VIEW SUBSYSTEMS"),
    ("4.", "DOWNLOAD"),
    ("5.", "EXIT"),
]

def print_banner():
    try:
        with open("banner.txt", "r") as file:
            banner_content = file.read()
            console.print(f"[royal_blue1]{banner_content}[/royal_blue1]")
    except FileNotFoundError:
        console.print("[bold red]Banner file not found![/bold red]")

def search_keyword(data, keyword):
    matching_items = []
    for item in data:
        for key, value in item.items():
            if key == "details":
                for k, v in value.items():
                    if keyword in k or keyword in v:
                        matching_items.append(item)
            else:
                if keyword in key or keyword in value:
                    matching_items.append(item)
    return matching_items

def scan_subsystem_items():
    input = select_subsystem()
    subtopic = select_subsystem_topic(input)
    url = get_url_from_subsystem(subtopic)
    result = scrape_site_with_pagination(url)
    data = json.loads(json.dumps(result))
    print_styled_items(data["items"])
    val = console.input("[cyan]Press Enter to Continue or (S to Search Keyword)...[/cyan]")

    while val == "S" or val == "s":
        keys = gather_all_keys(data["items"])
        search_key = console.input("[cyan]Enter Keyword to Search: [/cyan]")
        search_result = search_keyword(data["items"], search_key)
        print_styled_items_with_keyword_highlights(search_result, search_key)
        val = console.input("[cyan]Press Enter to Continue or (S to Search Keyword)...[/cyan]")

def scan_component():
    input = select_subsystem()
    subtopic = select_subsystem_topic(input)
    url = get_url_from_subsystem(subtopic)
    result = scrape_site_with_pagination(url)
    data = json.loads(json.dumps(result))["items"]
    component = select_component(input, data)
    component_url = component["link"]
    component_data = scrape_item(component_url)
    print_styled_component(component_data[0])

def view_subsystems():
    console.print("[bold green]Viewing subsystems...[/bold green]")
    display_subsystems()

def download_item_specific_page():
    item_name = console.input("[cyan]Enter the item name to download: [/cyan]")
    console.print(f"[bold green]Downloading item page for: {item_name}...[/bold green]")

def get_info_about_item():
    item_name = console.input("[cyan]Enter the item name for info: [/cyan]")
    console.print(f"[bold green]Fetching info about: {item_name}...[/bold green]")

def exit_program():
    console.print("[bold red]Exiting the program...[/bold red]")
    exit()

while True:
    menu_lines = "\n".join([f"[cyan]{item[0]}[/cyan] [bold]{item[1]}[/bold]" for item in menu_items])

    menu_panel = Panel(
        f"{menu_lines}",
        border_style="bright_magenta",
        expand=False,
    )
    
    print_banner()
    console.print(menu_panel)
    choice = console.input("[cyan]Please select an option (1-5): [/cyan]")

    if choice == "1":
        scan_subsystem_items()
    elif choice == "2":
        scan_component()
    elif choice == "3":
        display_subtopics()
    elif choice == "4":
        display_download_prompt()
    elif choice == "5":
        exit_program()
    else:
        console.print("[bold red]Invalid option. Please choose a number between 1 and 5.[/bold red]")

    console.input("[cyan]Press Enter to continue...[/cyan]")