from es import CSVFile
import unittest
class Test_getdata(unittest.TestCase):
  def test_init(self):
    csv_file = CSVFile('sha.csv')
    
#controllo se esiste un attributo nome
    self.assertEqual(csv_file.name, 'sha.csv')

  def test_getdata(self):
    self.assertEqual(csv_file.get_data(),)