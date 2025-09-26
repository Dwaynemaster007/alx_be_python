def display_menu():
    """Displays the main menu options to the user."""
    print("\nShopping List Manager 🛒")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function for the Shopping List Manager.
    Manages the shopping list based on user choices.
    """
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # 1. Add Item
            item = input("Enter the item to add: ").strip()
            if item: # Check if the input is not empty
                shopping_list.append(item)
                print(f"'{item}' added to the list.")
            else:
                print("Item name cannot be empty.")
            
        elif choice == '2':
            # 2. Remove Item
            if not shopping_list:
                print("The list is empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            
            try:
                # Attempt to remove the item. Python's list.remove() raises ValueError if item is not found.
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' removed from the list.")
            except ValueError:
                # Item not found handling
                print(f"Error: '{item_to_remove}' was not found in the list.")

        elif choice == '3':
            # 3. View List
            if shopping_list:
                print("\n--- Current Shopping List ---")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
                print("-----------------------------\n")
            else:
                print("The shopping list is currently empty.")

        elif choice == '4':
            # 4. Exit
            print("Goodbye! 👋")
            break
            
        else:
            # Invalid choice handling
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
