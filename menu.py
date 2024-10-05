import sys

class SatelliteCatalogCLI:
    def __init__(self):
        self.options = {
            '1': 'Download entire catalog',
            '2': 'Download a subsystem',
            '3': 'Download item specific page',
            '4': 'Get info about a specific item',
            '5': 'Exit'
        }

    def display_menu(self):
        print("\nSatellite Component Catalog CLI")
        print("=" * 30)
        for key, value in self.options.items():
            print(f"{key}. {value}")
        print("=" * 30)

    def execute_option(self, choice):
        if choice == '1':
            self.download_entire_catalog()
        elif choice == '2':
            self.download_subsystem()
        elif choice == '3':
            self.download_item_specific_page()
        elif choice == '4':
            self.get_info_about_item()
        elif choice == '5':
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice, please try again.")

    def download_entire_catalog(self):
        print("Downloading entire catalog...")
        # Implement download logic here
        # For now, just a placeholder
        print("Catalog downloaded successfully!")

    def download_subsystem(self):
        print("Downloading subsystem...")
        # Implement download logic here
        # For now, just a placeholder
        print("Subsystem downloaded successfully!")

    def download_item_specific_page(self):
        print("Downloading item specific page...")
        # Implement download logic here
        # For now, just a placeholder
        print("Item specific page downloaded successfully!")

    def get_info_about_item(self):
        item_id = input("Enter the ID or SKU of the item: ")
        print(f"Getting info about item with ID/SKU: {item_id}...")
        # Implement logic to get item info here
        # For now, just a placeholder
        print("Item information retrieved successfully!")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")
            self.execute_option(choice)

if __name__ == "__main__":
    cli = SatelliteCatalogCLI()
    cli.run()

