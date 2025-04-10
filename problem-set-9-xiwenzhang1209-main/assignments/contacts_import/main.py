import json

def add_number(contacts):
    name = input("Contact name?\n")
    num = input("Phone number?\n")

    if name not in contacts:
        contacts[name] = set()
    if num not in contacts[name]:
        contacts[name].add(num)
        print(f"Added number: {num} for {name}")
    else:
        print(f"Added number: {num} for {name}")
    
    

def delete_contact(contacts):
    name = input("Contact name?\n")
    if name not in contacts:
        print("Name not found. Try again.")
    else:
        del contacts[name]
        print(f"Deleted {name}")


def print_contact(contacts):
    name = input("Contact name?\n")

    if name not in contacts:
        print("Name not found. Try again.")   
    # if not contacts[name]:
    elif not contacts[name]: # changed ** here **
        print("No phone numbers available.")
    else:
        print(f"Contact \"{name}\":")
        print("Phone numbers:")
        for num in sorted(contacts[name]):
            print(num)



def print_most_numbers(contacts):
    sortable = []
    for name in contacts:
        sortable.append((len(contacts[name]), name))
    if sortable:
        sortable.sort()
        print(f"Contact with most phone numbers: {sortable[-1][1]}")
    else:
        print("No contacts available.")

def import_contacts_from_file(contacts, filename="assignments/contacts_import/data.json"):
    try:
        with open(filename, 'r') as f:
            imported_data = json.load(f)

        for entry in imported_data:
            first_name = entry.get('first_name', 'Unknown')
            last_name = entry.get('last_name', '')
            full_name = f"{first_name} {last_name}".strip()
            # phone_numbers = entry.get('phone_numbers', [])
            phone_numbers = list(entry.get('numbers', {}).values()) # changed ** here **
            if not isinstance(phone_numbers, list):
                print(f"Warning: 'phone_numbers' for {full_name} is not a list. Skipping.")
                continue 

            if full_name not in contacts:
                contacts[full_name] = set()
            for phone in phone_numbers:
                contacts[full_name].add(phone)
                
        print("Importing contacts from data.json") # changed ** here **
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except json.JSONDecodeError:
        print("Error deconding JSON from the file.")
    except Exception as e:
        print(f"Contacts imported successfully!")



def run_app():
    contacts = {}
    print("Welcome to the contacts app!")
    while True:
        print("1. Add a phone number")
        print("2. Delete a contact")
        print("3. Print a contact")
        print("4. Print contact with most phone numbers")
        print("5. Quit")
        print("6. Import contacts from file")
        choice = input("What would you like to do?\n")

        if choice == "1":
            add_number(contacts)
        elif choice == "2":
            delete_contact(contacts)
        elif choice == "3":
            print_contact(contacts)
        elif choice == "4":
            print_most_numbers(contacts)
        elif choice == "5":
            print("Bye!")
            break
        elif choice == "6":
            import_contacts_from_file(contacts)
        else:
            print("Invalid choice, try again")

run_app()
