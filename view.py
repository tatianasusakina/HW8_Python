def choice():
    print(f'Телефонный справочник!')
    print('-'*22)
    action = int(input('1 - Добавить контакт.\n2 - Поиск контакта.\n3 - Изменить контакт.\n4 - Удалить контакт.\n5 - Сортировать справочник.\n6 - Вывести весь справочник.\n7 - Выход из программы.\n'))
    return action


def get_data():
    surname = input('Введите фамилию контакта: ')
    name = input('Введите имя контакта: ')
    number = input('Введите номер: ')
    return f'{surname} {name} {number}'


def get_part_contact():
    part_contact = input('Введите данные поиска: ')
    return part_contact