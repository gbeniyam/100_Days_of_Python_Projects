import pprint

class phone_book():
    def __init__(self):
        self.phone_book_dict = dict()

    def add_contact(name="N/A", phone="Missing No.", email="No Email", category="No Category Specified"):
        """
        Add a new contact to the phone book
        Return True if added successfully, False if contact already exists
        example of categories: friend, family, work
        """
        if name != None:
            phone_book.phone_book_dict[name] = {
                "phone": phone,
                "email":email,
                "category": category
                }
            print(f"Added: {name}") # testing/dev print TODO: remove
            pprint.pprint(phone_book.phone_book_dict)
            return {name: phone_book.phone_book_dict[name]} # return added contact key:value pair
        else:
            print("Please provide a name")
            return

    def search_contact(name):
        """
        Search for a contact by name
        Return contact details if found, None if not found
        """
        if name != None:
            try:
                contact_details = phone_book.phone_book_dict[name]
                if contact_details != None:
                    return {name: contact_details}
                else:
                    return None # return 
            except Exception as e:
                print(f"An error occured: {e}")

    def get_contacts_by_category(category):
        """
        Return all contacts in a specific category
        """
        contact_matches = {k: v for k, v in phone_book.phone_book_dict.items() if v == category}
        pprint.pprint(contact_matches) # TODO test print, delete after
        return contact_matches

    def update_contact(name, phone, email, category): # defaults must be removed
        """
        Update a new contact in the phone book
        Return updated json data of contact (name, phone, email, category)
        example of categories: friend, family, work
        """
        print(f"update_contact for [\"{name}\"] Before update: ") # TODO remove after testing
        pprint.pprint(phone_book.phone_book_dict[name])
        
        if name != None:
            if phone != None:
                phone_book.phone_book_dict[name] = {
                    "phone": phone
                    }
            if email != None:
                phone_book.phone_book_dict[name] = {
                    "email":email
                    }
            if category != None:
                phone_book.phone_book_dict[name] = {
                    "category": category
                    }
            print(f"update_contact for [\"{name}\"] After update: ") # TODO remove after testing
            pprint.pprint(phone_book.phone_book_dict[name])
            
            return {name: phone_book.phone_book_dict[name]} # return updated contact key:value pair
        else:
            print("Please provide a name")
            return

    def delete_contact(name):
        """
        Delete contact by name
        Return "Contact Deleted" if successful or "Contact Not Found" if contact did not exist
        """
        if name != None:
            try:
                contact_removed = phone_book.phone_book_dict.pop(name)
            except Exception as e:
                print(e)
                return None
        print("Contact Deleted" if contact_removed else "Contact Not Found") # TODO talk to Marco about method return value.
        return contact_removed

# File called contacts.csv
# contact_name = phone_book["John Doe"]
def write_to_file(file, contact_name):
    """
    Write contact info to a file.
    Return Success on success, otherwise Fail and error message.
    """
    # contact_info_to_write = phone_book.search_contact(name="John Doe")
    # contact_info_to_write = {"John Doe", 555-0123, ...}
    # with_open...open file(contacts.csv)
    # csv library to add in row of data (contact_info_to_write)

# def read_from_file(file, )

def retreive_contact_from_file(file, name):
    """
    Retreive contact info from a file by name.
    Return contact info (phone, email, category)
    """

program_options = {
    1: add_contact,
    2: search_contact,
    3: get_contacts_by_category
}

# Example structure:
phone_book = {
    'John Doe': {
        'phone': '555-0123',
        'email': 'john@example.com',
        'category': 'work'
    },
    "Jane Doe": {
        'phone': "555-9876"
    }
}




def title_screen():
    title_art = """
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║           ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗            ║
║           ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝            ║
║           ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗              ║
║           ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝              ║
║           ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗            ║
║           ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝            ║
║               ██████╗  ██████╗  ██████╗ ██╗  ██╗                 ║
║               ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝                 ║
║               ██████╔╝██║   ██║██║   ██║█████╔╝                  ║
║               ██╔══██╗██║   ██║██║   ██║██╔═██╗                  ║
║               ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗                 ║
║               ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                 ║
║                                                                  ║
║                       MANAGER APPLICATION                        ║
║                                                                  ║
║                           Version 1.0.0                          ║
║                                                                  ║
║                     Press ENTER to continue...                   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
    print(title_art)
    input()


def welcome_screen():
    print("Welcome to the Phone Book Manager App\n")
    print("Select one of the following options:")

    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Get Contacts By Category")
    print("4. Update Contact")
    print("5. Delete Contact")


def menu_select()->int:
    # Continuously prompt user options
    try:
        user_input = int(input("Enter: "))
        return user_input
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1

def execute_menu_selection(usr_input:int):
    # add phone book as global, as it will be modified
    global phone_book

    # perform selection option
    if usr_input in program_options:
        selected_function = program_options[usr_input]

        if usr_input == 1:
            print("Add contact selected. Enter information ...")
            in_name = input("Name: ")
            in_phone = input("Phone: ")
            in_email = input("E-mail: ")
            in_category = input("Category: ")
            selected_function(phone_book, in_name, in_phone, in_email, in_category)
        elif usr_input == 2:

            pass
        elif usr_input == 3:
            pass
        else:
            print("Not valid option. Please Try again")
    else:
        print("Not a valid option. Please try again.")

def main():
    # title screen
    title_screen()

    # welcome user to phone book manager program
    welcome_screen()

    # Get user menu selection
    user_input = menu_select()

    # execute user menu selection
    execute_menu_selection(user_input)


if __name__ == "__main__":
    main()
