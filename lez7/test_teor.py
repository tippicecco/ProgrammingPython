import unittest
from math import pi
from teor import circle_area
#faccio testing
class TestSomma(unittest.TestCase):
  def test_somma(self):
    self.assertEqual(circle_area(1), pi)
    self.assertEqual(circle_area(0), 0)
    self.assertEqual(circle_area(2), pi * 2 ** 2)
  #when value is uncorrect
  def test_values(self):
    self.assertRaises(ValueError, circle_area, -2)

  def test_types(self):
    self.assertRaises(TypeError, circle_area, 2 + 5j)
    self.assertRaises(TypeError, circle_area, True)

