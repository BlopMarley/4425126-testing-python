def to_absolute(number):
    """
    >>> to_absolute(3)
    3
    >>> to_absolute(-3)
    3
    """
    """
    Return the absolute value

    :param number: Initial number
    :return:  The absolute value
    """
    # run test >>>python -m doctest -v exos/abs.py
    if number <= 0:
        return -number
    return number