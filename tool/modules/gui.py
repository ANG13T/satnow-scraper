from rich.console import Console
from rich.panel import Panel

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