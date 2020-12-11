from src import ex

def test_add1():
    assert ex.add_func(5,5) == 10

def test_add2():
    assert ex.add_func(5,10) == 15
