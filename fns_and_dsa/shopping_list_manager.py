def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    #While the shopping list is empty then display the menu above
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item to cart: ")
            shopping_list.append(item)
        elif choice == "2":
            item = input("Remove item from cart: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from cart.")
        elif choice == "3":
            if shopping_list:
                print("The following items are have beei added to your cart: ")
                for item in shopping_list:
                    print(item)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

