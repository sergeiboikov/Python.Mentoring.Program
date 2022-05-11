from decimal import Decimal

# Dictionary for currency courses. Courses related to Rubble
course = {"Rubble": Decimal(1), "Euro": Decimal(3), "Dollar": Decimal(2)}


class Currency:
    """
    Class for currency
    :param arg: Currency value
    :type arg: Decimal
    """

    def __init__(self, arg: Decimal):
        """Constructor method"""
        self._cur_value = arg

    @property
    def cur_name(self) -> str:
        """
        Property for currency name
        :return: Currency name
        :rtype: str
        """
        return self.__class__.__name__

    @property
    def cur_value(self) -> Decimal:
        """
        Property for currency value
        :return: Currency value
        :rtype: Decimal
        """
        return Decimal(self._cur_value)

    @property
    def course(self) -> Decimal:
        """
        Property for course value
        :return: Course value for currency by currency class name
        :rtype: Decimal
        """
        return course[self.__class__.__name__]

    @course.setter
    def course(self, cur_value: Decimal):
        """
        Setter for course value
        :param cur_value: Course value
        :type cur_value: Decimal
        """
        course[self.__class__.__name__] = Decimal(cur_value)

    def __str__(self) -> str:
        """
        Currency output
        :return: Currency value + currency symbol
        :rtype: str
        """
        cur_value = f"{self.cur_value} {self.symbol}"
        return cur_value

    def get_cur_value_by_currency(self, currency: object) -> Decimal:
        """
        Method returns currency value by currency name
        :param currency:
        :return:
        """
        if self.__class__ == currency:
            return self.cur_value
        else:
            # Convert another currency to current
            return self.to(currency).cur_value

    def __add__(self, other: object) -> object:
        """
        Method returns sum of currencies
        :param other_currency: object of :class:`Currency` to addition
        :type other_currency: object
        :return: object of :class:`Currency` as sum of currencies
        :rtype: object
        """
        return self.__class__(self.cur_value
                              + other.get_cur_value_by_currency(self.__class__))
        # Check if classes of currencies are equal

    def __radd__(self, other_cur_value: Decimal) -> object:
        """
        Method returns sum for iterates of currency values
        :param other_cur_value: Currency value
        :type other_cur_value: Decimal
        :return: object of :class:`Currency` as sum of currency values
        :rtype: object
        """
        return self.__class__(self.cur_value + other_cur_value)

    def __gt__(self, other: object) -> bool:
        """
        Method returns True if current currency value greater
        then currency value from another currency
        :param other: object of :class:`Currency`
        for comparing
        :type other: object
        :return: True if current currency value greater
        then currency value from another currency
        :rtype: bool
        """
        return self.cur_value > other.get_cur_value_by_currency(self.__class__)

    def __eq__(self, other: object) -> bool:
        """
        Method returns True if current currency value equal currency value
        from another currency
        :param other: object of :class:`Currency` for comparing
        :type other: object
        :return: True if current currency value equal currency value
        from another currency
        :rtype: bool
        """
        return self.cur_value == other.get_cur_value_by_currency(self.__class__)

    def __mul__(self, arg: float) -> object:
        """
        Method returns multiply of currency to the value
        :param arg: value for multiplying
        :type arg: float
        :return: object of :class:`Currency` as sum of currencies
        :rtype: object
        """
        return self.__class__(self.cur_value * arg)

    def __truediv__(self, arg: float) -> object:
        """
        Method returns division of currency to the value
        :param arg: value for division
        :type arg: float
        :return: object of :class:`Currency` as sum of currencies
        :rtype: object
        """
        return self.__class__(self.cur_value / arg)

    def to(self, other_currency: object) -> object:
        """
        Method converts current currency to another.
        Returns object of :class:`Currency` with converted currency value
        :param other_currency: child of :class:`Currency`.
        Target currency to conversion
        :type other_currency: object
        :return: object of :class:`Currency`. Target currency object
        :rtype: object
        """
        current_course = course[self.__class__.__name__]
        other_course = course[other_currency.__name__]
        n_curr = other_currency(current_course / other_course * self.cur_value)
        return n_curr


class Dollar(Currency):
    """
    Class for dollar
    """
    symbol = "$"

    @staticmethod
    def currency_course(other_currency: object) -> Decimal:
        """
        Method returns course of Dollar to another currency
        :param other_currency: child of :class:`Currency`.
        Currency for getting course
        :return: Course value
        :rtype: Decimal
        """
        return course["Dollar"] / course[other_currency.__name__]


class Euro(Currency):
    """
    Class for euro
    """
    symbol = "€"

    @staticmethod
    def currency_course(other_currency: object) -> Decimal:
        """
        Method returns course of Euro to another currency
        :param other_currency: child of :class:`Currency`.
        Currency for getting course
        :return: Course value
        :rtype: Decimal
        """
        return course["Euro"] / course[other_currency.__name__]


class Rubble(Currency):
    """
    Class for rubble
    """
    symbol = "₽"

    @staticmethod
    def currency_course(other_currency: object) -> Decimal:
        """
        Method returns course of Rubble to another currency
        :param other_currency: child of :class:`Currency`.
        Currency for getting course
        :return: Course value
        :rtype: Decimal
        """

        return course["Rubble"] / course[other_currency.__name__]


if __name__ == '__main__':
    d = Dollar(5)
    e = Euro(10)
    e2 = Euro(20)
    r = Rubble(2)

    print(f"d = {d}")
    print(f"e = {e}")
    print(f"e2 = {e2}")
    print(f"r = {r}")
    print(f"e.to(Dollar) = {e.to(Dollar)}")
    print(f"sum([Euro(i) for i in range(5)]) = "
          f"{sum([Euro(i) for i in range(5)])}")
    print(f"e > e2 = {e > e2}")
    print(f"e + d = {e + d}")
    print(f"d + e = {d + e}")
    print(f"e * 2 = {e * 2}")
    print(f"e / 2 = {e / 2}")

    e.course = 5
    print(f"e.to(Dollar) = {e.to(Dollar)}")
    print(f"e.currency = {e.cur_name}")

    print(f"Euro.currency_course(Rubble) = {Euro.currency_course(Rubble)}")
