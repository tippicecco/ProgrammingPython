import unittest
#from math import pi
from es import mod
from es import lista
from es import compute_incr
#faccio testing
class Testpred(unittest.TestCase):
  def test_prediction(self):
    self.assertEqual(mod.predict(lista), 65.0)
  def test_data(self):
    self.assertRaises(TypeError, compute_incr, [7,8,'c'])
    