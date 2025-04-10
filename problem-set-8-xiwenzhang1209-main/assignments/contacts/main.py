# TODO: your code here!
def main():
    def add_phone_number(contacts):
        name = input("Contact name?\n")
        phone = input("Phone number?\n")
        if name not in contacts:
            contacts[name] = set()
        if phone in contacts[name]:
            print(f"Added number: {phone} for {name}")
        else:
            contacts[name].add(phone)
            print(f"Added number: {phone} for {name}")

    def delete_contact(contacts):
        name = input("Contact name?\n")
        if name in contacts:
            del contacts[name]
            print(f"Deleted {name}")
        else:
            print("Name not found. Try again.")
        
    
    def print_contact(contacts):
        name = input("Contact name?\n")
        if name in contacts:
            print(f"Contact \"{name}\":")
            print("Phone numbers:")
            for number in sorted(contacts[name]):
                print(number)
        else:
            print("Name not found. Try again.")
    
    def find_contact_with_most_numbers(contacts):
        max_contact = None
        max_number = 0
        for contact in contacts:
            number_count = len(contacts[contact])
            if number_count > max_number:
               max_number = number_count
               max_contact = contact
        return max_contact

    def print_contact_with_most_numbers(contacts):
        if not contacts:
            print("No contacts available.")
            return
        max_contact = find_contact_with_most_numbers(contacts)
        print(f"Contact with most phone numbers: {max_contact}")
        


    contacts = {}

    print("\nWelcome to the contacts app!")
    while True:
        print("1. Add a phone number")
        print("2. Delete a contact")
        print("3. Print a contact")
        print("4. Print contact with most phone numbers")
        print("5. Quit")
        choice = input("What would you like to do?\n")

        if choice == "1":
            add_phone_number(contacts)
        elif choice == "2":
            delete_contact(contacts)
        elif choice == "3":
            print_contact(contacts)
        elif choice == "4":
            print_contact_with_most_numbers(contacts)
        elif choice == "5":   
            print("Bye!")
            break
        else:
            print("Invalid choice, try again")

main()