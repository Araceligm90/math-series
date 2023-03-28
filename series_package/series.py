def fibonacci(n):
    """
    Function that takes in a number and calculated the n of the Fibonacci sequence.
    :param n: number of the index we want to calculate.
    :return: the number of the index in the sequence.
    """
    if n < 0:
        return None
    elif n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Calculate n of the Lucas sequence.
    :parm n of the index to calculate
    :return: the n of the index in the Lucas sequence.
    """
    if n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """
    Function that takes in a value and two additional and optional ones. The first parameter will determine which
    element in the series to print. If the function is called ith no optional values it will produce a number from the
    Fibonacci series. If it's called with the optional 1 or 2, it will refer to the Lucas series.
    """
    if a == 0 and b == 1:
        return fibonacci(n)
    elif a == 2 and b == 1:
        return lucas(n)
