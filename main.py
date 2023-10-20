# Initialize an empty dictionary to represent the inventory.
inventory = {}
#only options for user to input
numbers = [1,2,3,4,5]
# Function to add items to the inventory.
def add_item():
    name = input("Enter the item name: ")
    quantity = (input("Enter the quantity: "))
    # if the user does not input an integer, print out and ask for an integer
    if quantity != numbers:
        print("Sorry, please enter a number value, not a word")
    # Check if the item is already in the inventory and update its quantity.
    if name in inventory:
        inventory[name] += quantity
    else:
        # If the item is not in the inventory, add it with the specified quantity.
        inventory[name] = quantity

# Function to remove items from the inventory.
def remove_item():
    name = input("Enter the item name to remove: ")
    
    # Check if the item is in the inventory.
    if name in inventory:
        quantity = int(input("Enter the quantity to remove: "))
        # if the user does not input an integer, print out and ask for an integer
        if quantity != numbers:
            print("Sorry, please enter a number value, not a word")
        # Check if there is enough of the item in the inventory to remove.
        if quantity <= inventory[name]:
            inventory[name] -= quantity
        else:
            print("Not enough of that item in the inventory.")
    else:
        print("Item not found in the inventory.")

# Function to view the current inventory.
def view_inventory():
    for item, quantity in inventory.items():
        print(f"{item}: {quantity} in stock")

# Function to search for items by name.
def search_item():
    name = input("Enter the item name to search for: ")
    
    # Check if the item is in the inventory and display its quantity.
    if name in inventory:
        print(f"{name} is in stock: {inventory[name]} available.")
    else:
        print(f"{name} is not in stock.")

while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Search Item")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    # Menu-driven program to perform various actions based on user input, both words and number.
    if choice == "1" or "one":
        add_item()
    elif choice == "2" or "two":
        remove_item()
    elif choice == "3" or "three":
        view_inventory()
    elif choice == "4" or "four":
        search_item()
    elif choice == "5" or "five":
        print("Exiting the program.")
        break
    else:
        # Handle invalid input from the user.
        print("Invalid choice. Please try again.")
