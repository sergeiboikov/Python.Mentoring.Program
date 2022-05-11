import random


class Matrix:
    """Class for matrix
    :param args: list (concrete matrix)
    or (int, int) - for generating a random matrix
    :type args: list or (int, int)"""

    def __init__(self, *args):
        """Constructor method"""
        # Number of arguments, that user has inputted
        self._numargs = len(args)

        if self._numargs == 1:
            # Check if user input list argument
            if isinstance(args[0], list):
                self._height = len(args[0])
                self._width = len(args[0][0])
                # Set matrix from the list, that was inputted by user
                self._rows = args[0]
            else:
                raise TypeError(f"Expected a list argument, "
                                f"got {args[0].__class__}")
        # If user pass two integer arguments set matrix as random matrix
        elif self._numargs == 2:
            # Check if user input two integer arguments
            if isinstance(args[0], int) and isinstance(args[1], int):
                self._width = args[0]
                self._height = args[1]
                # Set matrix as random matrix
                self._rows = self.random_matrix()
            else:
                raise TypeError(f"Expected 2 int arguments, "
                                f"got {args[0].__class__},"
                                f" {args[1].__class__}")
        else:
            raise TypeError(f"Expected at most 2 arguments, "
                            f"got {self._numargs}")

    def __str__(self):
        """Matrix output"""
        s = "\n".join([str(row_l) for row_l in self._rows])
        return s + '\n'

    @property
    def size(self) -> (int, int):
        """
        Method returns size of matrix
        :return: Size of matrix
        :rtype: int, int
        """
        return self._width, self._height

    def random_matrix(self) -> list:
        """
        Method returns list with self._height size
        of lists with self._width size
        :return: List with self._height size of lists
        with self._width size
        :rtype: list
        """
        matrix = list()
        for n in range(self._height):
            row = random.sample(range(0, 99), self._width)
            matrix.append(row)
        return matrix

    def reverse_matrix(self) -> object:
        """
        Method returns reversed object
        of :class:`Matrix`
        :return: reversed object of :class:`Matrix`
        :rtype: object
        """
        matrix = list()
        for n in range(self._height):
            row = self._rows[n]
            matrix.append(reversed(row))
        return Matrix(row)

    def transposition_matrix(self) -> object:
        """
        Method returns transposed object of :class:`Matrix`
        :return: transposed object of :class:`Matrix`
        :rtype: object
        """
        return Matrix([list(i) for i in zip(*self._rows)])

    def is_squared(self) -> bool:
        """
        Method returns True/False if matrix is squared or not
        :return: True/False if matrix is squared or not
        :rtype: bool
        """
        return self._width == self._height

    def __add__(self, other: object) -> object:
        """
        Method returns sum of matrices
        :param other: object of :class:`Matrix` to addition
        :type other: object
        :raise TypeError: Different size of matrices
        :return: object of :class:`Matrix` as sum of matrices
        :rtype: object
        """
        matrix = list()
        if self.size == other.size:
            for n in range(self._height):
                # new row as sum of matrices' rows
                row = [sum(item) for item in zip(self._rows[n],
                                                 other._rows[n])]
                matrix.append(row)
            return Matrix(matrix)
        else:
            raise TypeError("Different size of matrices")

    def __sub__(self, other: object) -> object:
        """
        Method returns substraction of matrices
        :param other: object of :class:`Matrix` to substract
        :type other: object
        :raise TypeError: Different size of matrices
        :return: object of :class:`Matrix` as substraction of matrices
        :rtype: object
        """
        matrix = list()
        if self.size == other.size:
            for n in range(self._height):
                row = [item[0] - item[1] for item in zip(self._rows[n],
                                                         other._rows[n])]
                matrix.append(row)
            return Matrix(matrix)
        else:
            raise TypeError("Different size of matrices")

    def _mul_skalar(self, arg):
        """
        Method returns multiply of matrix to scalar
        :param arg: Scalar value
        :type arg: int
        :return: object of :class:`Matrix` as multiply of matrix to scalar
        :rtype: object
        """
        matrix = list()
        for n in range(self._height):
            row = [item * arg for item in (self._rows[n])]
            matrix.append(row)
        return Matrix(matrix)

    def __mul__(self, other: object) -> object:
        """
        Method returns multiply of matrices (matrix to scalar)
        :param other: object of :class:`Matrix` to multiply
        :type other: object
        :raise TypeError: Different size of matrices
        :raise TypeError: Wrong argument type
        :return: object of :class:`Matrix` as multiply of matrices
        :rtype: object
        """
        matrix = list()
        # If we pass object of class Matrix - multiply matrix to matrix
        if other.__class__.__name__ == "Matrix":
            if self.size == other.size:
                for n in range(self._height):
                    row = [item[0] * item[1] for item in zip(self._rows[n],
                                                             other._rows[n])]
                    matrix.append(row)
                return Matrix(matrix)
            else:
                raise TypeError("Different rank of matrices")
        # If we pass scalar value - multiply matrix to the scalar value
        elif other.__class__.__name__ == "int":
            return self._mul_skalar(other)
        else:
            raise TypeError("Wrong argument type. Should be Matrix of Int")

    def is_equal(self, other: object) -> bool:
        """
        Method compares two matrices and returns if they are equal
        :param other: object of :class:`Matrix` to compare
        :type other: object
        :return: True/False if matrices are equal
        :rtype: bool
        """
        return self._rows == other._rows

    def is_symmetrical(self, diagonal: str = 'Main') -> bool:
        """
        Method returns if matrix is symmetrical
        :param diagonal: Diagonal for check symmetric
        (Possible values: 'Main', 'Side')
        :type diagonal: str
        :raise TypeError: Exceptions for incorrect diagonal value
        and unsquared matrices
        :return: True/False if matrix is symmetrical
        :rtype: bool
        """
        if self.is_squared():
            if diagonal == 'Main':
                return self.transposition_matrix() == self._rows
            elif diagonal == 'Side':
                reversed_matrix = self.reverse_matrix()
                return reversed_matrix.transposition_matrix() == self._rows
            else:
                raise TypeError("Choose correct diagonal: Main or Side")
        else:
            raise TypeError("Matrix is not squared")


if __name__ == '__main__':
    a = Matrix([[1, 2, 2], [3, 4, 9], [5, 6, 4]])
    b = Matrix(3, 3)

    print(f"Matrix A:\n{a}")
    print(f"Matrix B:\n{b}")
    # Sum
    print(f"A + B:\n{a + b}")
    # Subtraction
    print(f"A - B:\n{a - b}")
    # Multiply matrices
    print(f"A * B:\n{a * b}")
    # Multiply matrix to scalar
    print(f"A * 2:\n{a * 2}")
    # Matrix transposition
    print(f"Transposition A:\n{a.transposition_matrix()}")
    # If two matrices equal
    print(f"A equal B:\n{a.is_equal(b)}")
    # If matrix is squared
    print(f"A is squared:\n{a.is_squared()}")
    # If matrix is symmetrical
    print(f"A is symmetrical:\n{a.is_symmetrical(diagonal='Main')}")
