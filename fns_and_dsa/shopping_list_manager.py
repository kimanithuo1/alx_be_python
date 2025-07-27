def display_menu():
    print(f"Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")



def main():
    # Initialize an empty list to store the shopping list items
    shopping_list = []

    # This is the main loop for the program. It will continue to run until the user chooses to exit
    while True:
        # Display the menu so the user can make a choice
        display_menu()

        # Ask the user for their choice
        choice = input("Enter your choice: ")

        # If the user wants to add an item to the shopping list
        if choice == '1':
            # Ask the user for the item to add
            item = input("Enter the item to add: ").strip()

            # Add the item to the shopping list
            shopping_list.append(item)

            # Print out a message to let the user know that the item was added
            print(f"'{item}' has been added to your shopping list.")

        # If the user wants to remove an item from the shopping list
        elif choice == '2':
            # Ask the user for the item to remove
            item = input("Enter the item to remove: ").strip()

            # Check if the item is in the shopping list
            if item in shopping_list:
                # Remove the item from the shopping list
                shopping_list.remove(item)

                # Print out a message to let the user know that the item was removed
                print(f"'{item}' has been removed from your shopping list.")
            else:
                # Print out a message to let the user know that the item was not found in the shopping list
                print(f"'{item}' not found in the shopping list.")

        # If the user wants to view their shopping list
        elif choice == '3':
            # Check if the shopping list is empty
            if shopping_list:
                # Print out the shopping list
                print("\nYour Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                # Print out a message to let the user know that the shopping list is empty
                print("Your shopping list is empty.")

        # If the user wants to exit the program
        elif choice == '4':
            # Print out a message to let the user know that the program is exiting
            print("Goodbye!")

            # Break out of the loop to exit the program
            break

        # If the user enters an invalid choice
        else:
            # Print out a message to let the user know that the choice is invalid
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
