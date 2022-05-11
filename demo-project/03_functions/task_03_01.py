# Global variable for storing contacts
phonebook = [dict(name=None, number=None)]


def add_contact():
    """
    Function adds contact to phonebook
    :return: None
    """
    contact_info = dict(name=None, number=None)
    contact_name = input('Input contact name to add: ')
    contact_number = input('Input contact number to add: ')
    contact_info.update(name=contact_name, number=contact_number)
    phonebook.append(contact_info)
    print("Contact added successfully")


def get_contact():
    """
    Function gets contact from phonebook
    :return: None
    """
    col_names_t = ('имя', 'номер',)
    contact_name = input('Input contact name to get: ')
    print(f'{col_names_t[0]:20} | {col_names_t[1]:20}')
    for phonebook_item in phonebook:
        if phonebook_item.get('name') == contact_name:
            print(f'{contact_name:20} | {phonebook_item.get("number"):20}', )


def delete_contact():
    """
    Functions deletes contact from phonebook
    :return: None
    """
    contact_name = input('Input contact name to delete: ')
    for phonebook_item in phonebook:
        if phonebook_item.get('name') == contact_name:
            phonebook_item.clear()
        else:
            print(f"The contact {contact_name} isn't found")


def close_menu():
    """
    Function to exit the program
    :return: None
    """
    exit()


def get_action() -> int:
    """
    Function gets an action number for running the function
    from actions_dict dictionary
    :return: int
    """
    print('0: Add contact')
    print('1: Get contact')
    print('2: Delete contact')
    print('3: Close menu')
    return int(input('Select action: '))


# Dictionary with possible actions of the program
actions_dict = {0: add_contact,
                1: get_contact,
                2: delete_contact,
                3: close_menu}

if __name__ == '__main__':
    while True:
        a = get_action()
        actions_dict[a]()
