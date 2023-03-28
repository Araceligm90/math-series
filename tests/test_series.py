# there must be a function that starts with test (line 5)
# @pytest.mark.skip() --> deactivates function
# if what is being asserted is truthy it passes, if it's falsy the test fails. (line 9)

from series_package.series import fibonacci

from series_package.series import lucas

from series_package.series import sum_series


def test_fibonacci_exists():
    assert fibonacci


def test_fibonacci_1():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_2():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_3():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


def test_fibonacci_4():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_negative():
    actual = fibonacci(-1)
    expected = None
    assert actual == expected


def test_lucas_exists():
    assert lucas


def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_2():
    actual = lucas(5)
    expected = 11
    assert actual == expected


def test_lucas_3():
    actual = lucas(10)
    expected = 123
    assert actual == expected


def test_lucas_negative():
    actual = lucas(-1)
    expected = None
    assert actual == expected


def test_sum_series_exists():
    assert sum_series


def test_sum_series_1():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


def test_sum_series_2():
    actual = sum_series(2)
    expected = 1
    assert actual == expected


def test_sum_series_3():
    actual = sum_series(1, 1, 1)
    expected = 1
    assert actual == expected

