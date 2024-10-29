from rich.console import Console
from rich.panel import Panel
import re

console = Console()

def display_menu_prompt(items, color, expand):
    menu_lines = "\n".join([f"[cyan]{item[0]}[/cyan] [bold]{item[1]}[/bold]" for item in items])
    menu_panel = Panel(
        f"{menu_lines}",
        border_style=color,
        expand=expand,
    )
    console.print(menu_panel)
    choice = console.input(f"[cyan]Please select an option (1-{len(items)}): [/cyan]")
    return choice

def print_line(contents, style):
    console.print(f"[{style}]{contents}[/{style}]")

def print_input(contents, style):
    return console.input(f"[{style}]{contents}[/{style}]")

def print_styled_items(items):
    print("\n")
    for item in items:
        print_line("=" * 70, "bold magenta")
        for key, value in item.items():
            if key == "details":
                for k, v in value.items():
                    console.print(f"[magenta bold]{k.upper()}[/magenta bold] {v}")
            else:
                console.print(f"[magenta bold]{key.upper()}[/magenta bold] {value}")

def highlight_keyword(text, keyword):
    return re.sub(f"({re.escape(keyword)})", r"[bold yellow]\1[/bold yellow]", text, flags=re.IGNORECASE)

def print_styled_items_with_keyword_highlights(items, keyword):
    print("\n")
    for item in items:
        console.print("=" * 70, style="bold magenta")
        for key, value in item.items():
            if key == "details":
                for k, v in value.items():
                    highlighted_v = highlight_keyword(str(v), keyword)
                    console.print(f"[magenta bold]{k.upper()}[/magenta bold] {highlighted_v}")
            else:
                highlighted_value = highlight_keyword(str(value), keyword)
                console.print(f"[magenta bold]{key.upper()}[/magenta bold] {highlighted_value}")

def print_styled_component(component):
    for key, value in component['product_details'].items():
        console.print(f"[magenta bold]{key.upper()}:[/magenta bold] {value}")
    for key, value in component['general_parameters'].items():
        console.print(f"[magenta bold]{key.upper()}:[/magenta bold] {value}")
    console.print(f"[magenta bold]{'Manufacturer Website Link'.upper()}:[/magenta bold] {component.get('manufacturer_website_link', 'N/A')}")
    console.print(f"[magenta bold]URL:[/magenta bold] {component['url']}")