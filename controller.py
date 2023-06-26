from view import *
from database import *


def main():
    action = choice()
    while True:
        if action == 1:
            contact = get_data()
            add_contact(contact)
        elif action == 2:
            search = get_part_contact()
            find_contact(search)
        elif action == 3:
            search = get_part_contact()
            change_contact(search)
        elif action == 4:
            search = get_part_contact()
            del_contact(search)
        elif action == 5:
            sort_phonebook()
        elif action == 6:
            print_contacts()
        elif action == 7:
            print('Всего доброго!')
            break
        action = choice()