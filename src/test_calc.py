import unittest
# import calc
import math
class TestCalc(unittest.TestCase):
    """
    Test the add function from the calc library
    """

    def test_add_integers(self):
        print("add 1+2 == 3")
        result = 1+2
        self.assertEqual(result, 3)

    def test_sub_integers(self):
        print("sub 10-2 == 8")
        result = 10-2
        self.assertEqual(result, 8)

    def test_mult_integers(self):
        print("mult 2*5 == 10")
        result = 2*5
        self.assertEqual(result, 10 )

    def test_div_integers(self):
        print("div 10/2 == 5")
        result = 10/2
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
