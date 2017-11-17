"""This is the test of the program function_medium"""
def func(x, y):
    """func is a fnction with two parameter
    """
    return x + y
def test_func():
    """This function is used for test
    """
    assert func(2, 5) == 8

