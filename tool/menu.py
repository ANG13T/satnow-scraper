from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from modules.display import display_subsystems
from modules.download import display_download_prompt

console = Console()

# Scan should soley print and download should present options (entire [breakdown process] + subsystem + specific item) 
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

def download_entire_catalog():
    console.print("[bold green]Downloading entire catalog...[/bold green]")

def download_subsystem():
    subsystem_name = console.input("[cyan]Enter the subsystem name to download: [/cyan]")
    console.print(f"[bold green]Downloading subsystem: {subsystem_name}...[/bold green]")

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

# Create the title and menu text
title = Text("Satellite Component Catalog CLI", style="bold white on #1f1f7a", justify="center")

while True:
    # Construct the menu
    menu_lines = "\n".join([f"[cyan]{item[0]}[/cyan] [bold]{item[1]}[/bold]" for item in menu_items])
    
    # Create a panel to display the menu
    menu_panel = Panel(
        f"{menu_lines}",
        border_style="bright_magenta",
        expand=False,
    )
    
    print_banner()

    # Print the styled menu
    console.print(menu_panel)

    # Get user input
    choice = console.input("[cyan]Please select an option (1-5): [/cyan]")
    
    # Execute the corresponding action
    if choice == "1":
        download_entire_catalog()
    elif choice == "2":
        download_subsystem()
    elif choice == "3":
        display_subsystems()
    elif choice == "4":
        display_download_prompt()
    elif choice == "5":
        exit_program()
    else:
        console.print("[bold red]Invalid option. Please choose a number between 1 and 5.[/bold red]")

    # Add a pause after each operation
    console.input("[cyan]Press Enter to continue...[/cyan]")

