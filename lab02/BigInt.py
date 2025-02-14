class BigInt:
    """
    A class that can represent an integer of any size using a list of integers with no more than 4 digits each

    For instance, the integer 1234567890123456789012345678901234567890 could be represented as:
    [1234, 5678, 9012, 3456, 7890, 1234, 5678, 9012, 3456, 7890]

    If there are zeros in certain places in the number, they will not be shown in chunks, for instance:
    123400567890 could be represented as: [1234, 56, 7890] and it is assumed that 56 means 0056, not 56

    Please note that integers can be negative as well. In this case, the isNegative attribute will be set to True

    You must implement all the methods in this file, though you may define additional helper methods if you wish

    You may not import any libraries or use any built-in Python data structures or methods, and you may not ever
    have the number represented as a single int in any situation. You must always use the list of integers.
    """

    def __init__(self, num: str):
        """
        creates a BigInt object from a string representation of an integer
        This method will automatically be called when you create a new BigInt object like this: my_big_int = BigInt("12")
        :param num: the string representation of the integer
        """
        self.chunks = []  # list of integers with no more than 4 digits each
        self.isNegative = False  # whether the number is negative

    def __str__(self) -> str:
        """
        returns the string representation of the integer with commas every 3 digits (just like a normal number)
        This method will automatically be called when you cast a BigInt object to a string like this: str(my_big_int)
        or if you print a BigInt object like this print(my_big_int)
        example:
            If the BigInt object had the number [1234, 5678, 9012], this method would return "123,456,789,012"
            And if that BigInt was negative, it would return "-123,456,789,012"
        :return: the string representation of the integer with commas every 3 digits
        """
        pass

    def __eq__(self, other) -> bool:
        """
        checks if two BigInt objects represent the same number (are equal)
        This method will automatically be called when you use the == or != operators to compare two BigInt objects
        :param other: the other BigInt object
        :return: True if they are equal, False otherwise
        """
        return str(self) == str(other)

def add(a: BigInt, b: BigInt) -> BigInt:
    """
    adds two BigInt objects together
    :param a: the first BigInt object
    :param b: the second BigInt object
    :return: the BigInt object that represents a + b
    """
    pass


def subtract(a: BigInt, b: BigInt) -> BigInt:
    """
    subtracts the second BigInt object from the first BigInt object
    :param a: the first BigInt object
    :param b: the second BigInt object
    :return: the BigInt object that represents a - b
    """
    pass


def multiply(a: BigInt, b: BigInt) -> BigInt:
    """
    multiplies two BigInt objects together
    :param a: the first BigInt object
    :param b: the second BigInt object
    :return: the BigInt object that represents a * b
    """
    pass


def divide(a: BigInt, b: BigInt) -> BigInt:
    """
    performs integer division of the first BigInt object by the second BigInt object
    integer division means that the remainder is discarded, so the integer division of 5 by 2 is 2, not 2.5
    :param a: the first BigInt object
    :param b: the second BigInt object
    :raise: ZeroDivisionError if b is 0
    :return: the BigInt object that represents a // b
    """
    # use this line if b is 0:
    # raise ZeroDivisionError()

    pass

def modulo(a: BigInt, b: BigInt) -> BigInt:
    """
    performs the modulo operation of the first BigInt object by the second BigInt object
    the modulo operation is the remainder after integer division. If either a or b is negative, the result will be
    either negative or 0, but never positive. Other than that, the operation is the same regardless of the sign of a or b.
    :param a: the first BigInt object
    :param b: the second BigInt object
    :return: the BigInt object that represents a % b
    """
    pass


def main():
    """
    This is provided for you to test the BigInt class and the functions you write
    These will not be the only tests that your code will be run against, so make sure to test thoroughly yourself
    Feel free to change this code as you wish, but do not change the name of this method or the
    if __name__ == "__main__":
    part at the end
    """
    a_str = "123456789012"
    a = BigInt(a_str)
    assert len(a.chunks) == 3
    assert a.isNegative == False
    assert str(a) == "123,456,789,012"
    assert a == BigInt(a_str)

    b_str = "-3456789012"
    b = BigInt(b_str)
    assert b.chunks == [34, 5678, 9012]
    assert b.isNegative == True
    assert str(b) == "-3,456,789,012"
    assert b == BigInt(b_str)
    assert a != b

    c = BigInt("123400567890")
    assert str(c) == "123,400,567,890"

    assert str(add(a, a)) == "246,913,578,024"
    assert str(add(b, b)) == "-6,913,578,024"
    assert add(a, b) == add(b, a)

    assert str(subtract(a, a)) == "0"
    assert str(subtract(a, b)) == "126,913,578,024"

    assert str(multiply(b, b)) == "11,949,390,273,483,936,144"
    assert multiply(b, a) == multiply(a, b)

    assert str(divide(a, a)) == "1"
    assert str(divide(a, b)) == "-35"
    c = BigInt("0")
    try :
        divide(a, c)
        assert False
    except ZeroDivisionError:
        pass

    assert str(modulo(a, a)) == "0"
    assert str(modulo(a, b)) == "-2,469,173,592"

    print("All tests pass!")


if __name__ == "__main__":
    main()
