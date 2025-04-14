import unittest 
from math_utils import add, subtract

class TestMathUtils(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(3, 10), 13)
    self.assertEqual(add(-5, 15), 10)

  def test_subtract(self):
    self.assertEqual(subtract(20, 2), 18)
    self.asserEqual(subtract(0, 0), 0)

if __name__ == '__main__':
  unittest.main()
