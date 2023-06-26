from view import *


def add_contact(contact):
    with open('/Users/Eduard/Desktop/GeekBrains/Python_Lessons/Python_Lessons/HomeWork_8/phonebook.txt', 'a', encoding='utf-8') as file:
        print(contact.lower(), file=file)
    print(f'Контакт "{contact}" добавлен в справочник!')


def print_contacts():
    with open('/Users/Eduard/Desktop/GeekBrains/Python_Lessons/Python_Lessons/HomeWork_8/phonebook.txt', 'r', encoding='utf-8') as file:
        for line in file:
            print(' '.join(map(str.title, line.split())))


def find_contact(data):
    with open('/Users/Eduard/Desktop/GeekBrains/Python_Lessons/Python_Lessons/HomeWork_8/phonebook.txt', 'r', encoding='utf-8') as file:
        contacts = [line.strip().title()
                    for line in file if data.lower() in line]
        if contacts:
            print(f'Контакты по запросу "{data}"')
            print(*contacts, sep='\n')
        else:
            print('Контакта с такими данными нету!')


def change_contact(data):
    with open('/Users/Eduard/Desktop/GeekBrains/Python_Lessons/Python_Lessons/HomeWork_8/phonebook.txt', 'r', encoding='utf-8') as file:
        contacts = [line.strip() for line in file]
        other_contacts = [i for i in contacts if data.lower() not in i]
        change_contacts = [i for i in contacts if data.lower() in i]
        new_contacts = []
        if len(change_contacts) == 0:
            print('Контакта с такими данными нету!')
            new_contacts = other_contacts[:]
        elif len(change_contacts) == 1:
            print(*[i.title() for i in change_contacts])
            print('Данные для изменения контакта!')
            data = get_data()
            print(f'Контакт изменен на "{data}"')
            new_contacts = other_contacts + [data]
        elif len(change_contacts) > 1:
            for indx, contact in enumerate([i.title() for i in change_contacts], 1):
                print(f'{indx}. {contact}')
            con_num = int(
                input('Введите цифру котакта, который нужно изменить!\n'))
            print('Данные для изменения контакта!')
            data = get_data()
            print(f'Контакт изменен на "{data}"')
            change_contacts[con_num-1] = data
            new_contacts = other_contacts + change_contacts
        with open('/Users/Eduard/Desktop/GeekBrains/Python_Lessons/Python_Lessons/HomeWork_8/phonebook.txt', 'w', encoding='utf-8') as file:
            for contact in new_contacts:
                print(contact.lower(), file=file)


def del_contact(data):
    with open('/Users/Eduard/Desktop/GeekBrains/Python_Lessons/Python_Lessons/HomeWork_8/phonebook.txt', 'r', encoding='utf-8') as file:
        contacts = [line.strip() for line in file]
        other_contacts = [i for i in contacts if data.lower() not in i]
        change_contacts = [i for i in contacts if data.lower() in i]
        new_contacts = []
        if len(change_contacts) == 0:
            print('Контакта с такими данными нету!')
            new_contacts = other_contacts[:]
        elif len(change_contacts) == 1:
            print(*[i.title() for i in change_contacts])
            print(f'Контакт удален!')
            new_contacts = other_contacts[:]
        elif len(change_contacts) > 1:
            for indx, contact in enumerate([i.title() for i in change_contacts], 1):
                print(f'{indx}. {contact}')
            con_num = int(
                input('Введите цифру котакта, который нужно удалить!\n'))
            print(f'Контакт удален')
            del change_contacts[con_num-1]
            new_contacts = other_contacts + change_contacts
        with open('/Users/Eduard/Desktop/GeekBrains/Python_Lessons/Python_Lessons/HomeWork_8/phonebook.txt', 'w', encoding='utf-8') as file:
            for contact in new_contacts:
                print(contact.lower(), file=file)


def sort_phonebook():
    print('По какому признаку сортировать справочник?')
    num = int(input('1 - по фамилии.\n2 - по имени.\n3 - по номеру телефона.\n'))
    with open('/Users/Eduard/Desktop/GeekBrains/Python_Lessons/Python_Lessons/HomeWork_8/phonebook.txt', 'r', encoding='utf-8') as file:
        contacts = sorted([line.strip() for line in file],
                          key=lambda x: x.split()[num-1])
    with open('/Users/Eduard/Desktop/GeekBrains/Python_Lessons/Python_Lessons/HomeWork_8/phonebook.txt', 'w', encoding='utf-8') as file:
        for line in contacts:
            print(line, file=file)