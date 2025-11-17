from phonebook import PhoneBook
import pprint

valid_options = {
    "1": "Add Contact",
    "2": "Search Contact",
    "3": "Get Contacts By Category",
    "4": "Update Contact",
    "5": "Delete Contact",
    "q": "Quit Program"
}


if __name__ == "__main__":
    phoneBook = PhoneBook()
    user_input = None

    test_data = {
    'Alice Johnson': {
        'phone': '555-1024',
        'email': 'alice.johnson@example.com',
        'category': 'friend'
    },
    'Michael Smith': {
        'phone': '555-4432',
        'email': 'michael.smith@example.com',
        'category': 'work'
    },
    'Sara Kim': {
        'phone': '555-7789',
        'email': 'sara.kim@example.com',
        'category': 'family'
    },
    'David Patel': {
        'phone': '555-6390',
        'email': 'david.patel@example.com',
        'category': 'friend'
    },
    'Emily Carter': {
        'phone': '555-2219',
        'email': 'emily.carter@example.com',
        'category': 'work'
    },
    'Marcus Lee': {
        'phone': '555-5644',
        'email': 'marcus.lee@example.com',
        'category': 'family'
    },
    'Olivia Nguyen': {
        'phone': '555-8841',
        'email': 'olivia.nguyen@example.com',
        'category': 'friend'
    },
    'Henry Wallace': {
        'phone': '555-4477',
        'email': 'henry.wallace@example.com',
        'category': 'work'
    },
    'Natalie Brooks': {
        'phone': '555-3308',
        'email': 'natalie.brooks@example.com',
        'category': 'family'
    },
    'Trevor Adams': {
        'phone': '555-7772',
        'email': 'trevor.adams@example.com',
        'category': 'friend'
    }
}
    
    # Test1: Add all contacts from test_data to phoneBook
    for name, info in test_data.items():
        phoneBook.add_contact(name=name, phone=info["phone"], email=info["email"], category=info["category"])
    
    pprint.pprint(phoneBook.phone_book_dict)
    
    # Test2: Search all contacts from test_data in the phoneBook
    # Test3: Get all contacts by category: test each category
    # Test4: Update all four fields of one individual contact
    # Test5: Go through test data and delete all contacts from phoneBook
