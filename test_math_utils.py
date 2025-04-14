import unittest
from math_utils import add, subtract

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(100, 36), 136)
        self.assertEqual(add(5200, 4000), 9200)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-20, -10), -30)

if __name__ == '__main__':
    unittest.main()
