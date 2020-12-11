from src import ex
import unittest
class TestCase(unittest.TestCase):

    def test_add1(self):
        assert ex.add_func(5,5) == 10

    def test_add2(self):
        assert ex.add_func(5,10) == 15
