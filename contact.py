# Initialize an empty dictionary to store contacts
contact_book = {}

def add_contact(name, phone, email):
    """
    Add a new contact to the contact book.
    Args:
        name (str): Contact's name.
        phone (str): Contact's phone number.
        email (str): Contact's email address.
    """
    contact_book[name] = {"phone": phone, "email": email}
    print(f"Added contact {name}.")

def view_contacts():
    """Display all saved contacts."""
    if not contact_book:
        print("No contacts found.")
    else:
        for name, details in contact_book.items():
            print(f"{name}: Phone - {details['phone']}, Email - {details['email']}")

def search_contact(query):
    """
    Search for a contact by name or phone number.
    Args:
        query (str): Search query (name or phone number).
    """
    found_contacts = []
    for name, details in contact_book.items():
        if query.lower() in name.lower() or query in details["phone"]:
            found_contacts.append(name)
    if found_contacts:
        print(f"Found contacts matching '{query}': {', '.join(found_contacts)}")
    else:
        print(f"No contacts found for '{query}'.")

def update_contact(name, new_phone=None, new_email=None):
    """
    Update contact details.
    Args:
        name (str): Contact's name.
        new_phone (str, optional): New phone number. Defaults to None.
        new_email (str, optional): New email address. Defaults to None.
    """
    if name in contact_book:
        if new_phone:
            contact_book[name]["phone"] = new_phone
        if new_email:
            contact_book[name]["email"] = new_email
        print(f"Updated contact {name}.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    """Delete a contact."""
    if name in contact_book:
        del contact_book[name]
        print(f"Deleted contact {name}.")
    else:
        print(f"Contact '{name}' not found.")

# Example usage
if __name__ == "__main__":
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            query = input("Enter search query (name or phone number): ")
            search_contact(query)
        elif choice == "4":
            name = input("Enter contact name to update: ")
            new_phone = input("Enter new phone number (leave blank to skip): ")
            new_email = input("Enter new email address (leave blank to skip): ")
            update_contact(name, new_phone, new_email)
        elif choice == "5":
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == "6":
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice. Please select a valid option.")