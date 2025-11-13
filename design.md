# Design doc for phonebook.py
class phone_book
class contact (later), used within phone_book

methods in phone_book (CRUD):
add_contact
search_contact
get_contacts_by_category
update_contact
delete_contact

main:
1. print intro (title and welcome screen) to output
    a. include menu selection (1-5, functions above)
2. prompt user for input
3. handle input accordingly
    a. add_contact: add a contact to dict() type
    b. search contact: search dict() phone_book object for contact
    c. etc

object interaction notes:
Initialize phone_book object in main
pb object will contain dict() and be made accessible
    by the rest of the program
pb obj will be passed around through methods as needed