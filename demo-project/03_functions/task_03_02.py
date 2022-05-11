from typing import Callable

# Initial dataset
friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол',
     'email': 'email@email.com'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол',
     'email': 'email1@email1.com'}
]


def select(*field_name: list) -> Callable:
    """
    Function takes list of fields that should be in result set
    :param field_name: list of fields that should be in result set
    :type field_name: list
    :return: Function for selection
    :rtype: Callable
    """

    def select_inner(collection: dict) -> dict:
        """
        Function takes dict for selection and returns dict with selected items
        :param collection: Collection for selection
        :type: collection: dict
        :return: Dictionary with selected items from the collection
        :rtype: dict
        """
        selected_dict = {key: collection.get(key) for key in field_name}
        return selected_dict

    return select_inner


def field_filter(field_name: str, values_collection: list) -> Callable:
    """
    Function takes field name for filtration and an iterable object -
    list of values that should be in result set
    :param field_name: field name for filtration
    :type field_name: str
    :param values_collection: iterable object -
    list of values that should be in result set
    :type values_collection: list
    :return: Fuction for filtration
    :rtype: Callable
    """

    def field_filter_inner(collection: dict) -> bool:
        """
        Function takes collection for filtration
        and returns True or False according to result of the filtration
        :param collection: Collection for filtration
        :type dict
        :return: Result according to filtration
        :rtype: bool
        """
        return collection.get(field_name) in values_collection

    return field_filter_inner


def query(collection: list, select: Callable,
          *field_filters: Callable) -> list:
    """
    Function that selects needed fields and filters them
    :param collection: Input list of dicts for selection and filtration
    :type collection: list
    :param select: Function for selection
    :type select: Callable
    :param field_filters: Functions for filtration
    :type field_filters: Callable

    :return: List of selected and filtered dicts
    :rtype: list
    """
    return [select(item) for item in collection
            if all([field_filter(item) for field_filter in field_filters])]


if __name__ == '__main__':
    result = query(
        friends,
        select('name', 'gender', 'sport'),
        field_filter('sport', ['Баскетбол', 'Волейбол']),
        field_filter('gender', ['Мужской']),
    )
    print(result)
