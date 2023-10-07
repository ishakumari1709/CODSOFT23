contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")

    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"{name} has been added to your contacts.")

def view_contacts():
    if not contacts:
        print("Your contacts list is empty.")
    else:
        print("Contact List:")
        for name, details in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            print("-" * 20)

def search_contact():
    search_term = input("Enter the name or phone number to search: ").lower()
    found = False

    for name, details in contacts.items():
        if search_term in name.lower() or search_term in details["Phone"]:
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Current details for {name}:")
        print(f"Phone: {contacts[name]['Phone']}")
        print(f"Email: {contacts[name]['Email']}")
        print(f"Address: {contacts[name]['Address']}")
        
        contacts[name]["Phone"] = input("Enter new phone number (press Enter to keep it unchanged): ")
        contacts[name]["Email"] = input("Enter new email (press Enter to keep it unchanged): ")
        contacts[name]["Address"] = input("Enter new address (press Enter to keep it unchanged): ")
        
        print(f"{name}'s contact details have been updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from your contacts.")
    else:
        print("Contact not found.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Select an option (1/2/3/4/5/6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please choose a valid option.")
