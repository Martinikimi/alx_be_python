def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # ✅ this is the array (list) ALX expects

    while True:
        display_menu()  # ✅ must explicitly call this function every loop

        try:
            choice = int(input("Enter your choice (1-4): "))  # ✅ choice as a number
        except ValueError:
            print("Invalid input. Please enter a number (1-4).")
            continue

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"✅ {item} added to your list.")

        elif choice == 2:
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"❌ {item} removed from your list.")
            else:
                print("Item not found in list.")

        elif choice == 3:
            print("\n🛒 Your Shopping List:")
            if shopping_list:
                for i, itm in enumerate(shopping_list, start=1):
                    print(f"{i}. {itm}")
            else:
                print("(Empty List)")
            print()

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number 1-4.")

if __name__ == "__main__":
    main()






