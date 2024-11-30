from rich import print
from rich.tree import Tree
from rich.console import Console
from modules.config import OUTLINE, SUBSYSTEMS, SUBSUBSYSTEMS_URLS, SUBSUBSYSTEMS

console = Console()

def display_subtopics():
    tree = Tree("\n [bold white]🛰️  SATELLITE SUBSYSTEMS", guide_style="bold #5f00ff")
    for category, components in OUTLINE.items():
        category_branch = tree.add(f"[bold #a500ff]{category}")

        for component in components:
            category_branch.add(f"[#00d7ff]{component}")

    print(tree)

def get_url_from_subsystem(subsystem_name):
    for item in SUBSUBSYSTEMS_URLS:
        if item['item'] == subsystem_name:
            return item['url']

def get_subtopics_by_index(index):
    subsystem_names = list(OUTLINE.keys())

    if 0 <= index < len(subsystem_names):
        subsystem_name = subsystem_names[index]
        return OUTLINE[subsystem_name]
    else:
        raise IndexError("Subsystem index out of range.")
def select_subsystem():
    console.print("\n[bold white]🛰️  SATELLITE SUBSYSTEMS[/bold white]")
    try:
        # Display the options
        for i, category in enumerate(OUTLINE):
            console.print(f"[bold #a500ff]{i + 1}: {category}[/bold #a500ff]")
        # Get user input
        choice = console.input(f"[cyan]Please select an option (1-{len(OUTLINE)}): [/cyan]").strip()
        # Check for empty input
        if not choice:
            console.print("[bold red]No input detected. Please enter a number.[/bold red]")
            return None  # Gracefully return to the caller
        # Attempt to convert input to an integer
        choice = int(choice)
        # Ensure choice is within a valid range
        if choice < 1 or choice > len(OUTLINE):
            console.print(f"[bold red]Invalid choice. Please select a number between 1 and {len(OUTLINE)}.[/bold red]")
            return None
        return choice - 1
    except ValueError as e:
        console.print(f"[bold red]Invalid input. Please enter a valid number: {e}[/bold red]")
        return None
    except Exception as e:
        console.print(f"[bold red]An unexpected error occurred: {e}[/bold red]")
        return None



def select_subsystem_topic(subsystem_index):
    print("\n[bold white]🛰️  SUBSYSTEM TOPICS[/bold white]")
    subsystem_name = list(OUTLINE.keys())[subsystem_index]
    subtopics = get_subtopics_by_index(subsystem_index)
    for i, category in enumerate(subtopics):
        print(f"[bold #a500ff]{i + 1}: {category}[/bold #a500ff]")
    choice = console.input(f"[cyan]Please select an option (1-{(len(subtopics))}): [/cyan]")
    return subtopics[int(choice) - 1]

def select_component(subsystem_index, components):
    print("\n[bold white]🛰️  COMPONENTS[/bold white]")
    subsystem_name = list(OUTLINE.keys())[subsystem_index]
    subtopics = get_subtopics_by_index(subsystem_index)
    for i, category in enumerate(components):
        print(f"[bold #a500ff]{i + 1}: {category['title']}[/bold #a500ff]")
    choice = console.input(f"[cyan]Please select an option (1-{(len(components))}): [/cyan]")
    return components[int(choice) - 1]