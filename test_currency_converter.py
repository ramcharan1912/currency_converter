import unittest
from currency_converter import dollar_to_rupee, rupee_to_dollar 

class TestCurrencyConversion(unittest.TestCase):

      def test_dollar_to_rupee(self):
        self.assertAlmostEqual(dollar_to_rupee(10), 740)
        self.assertAlmostEqual(dollar_to_rupee(20), 1480)

      def test_blank_input_dollar_to_rupee(self):
        with self.assertRaises(ValueError):
            dollar_to_rupee('') 

      def test_non_numeric_input_dollar_to_rupee(self):
        with self.assertRaises(ValueError):
            dollar_to_rupee('value') 

      def test_negative_input_dollar_to_rupee(self):
        with self.assertRaises(ValueError):
            dollar_to_rupee(-10) 

      def test_rupee_to_dollar(self):
        self.assertAlmostEqual(rupee_to_dollar(740), 10)
        self.assertAlmostEqual(rupee_to_dollar(1480), 20) 

      def test_blank_input_rupee_to_dollar(self):
          with self.assertRaises(ValueError):
            rupee_to_dollar('')                  
         
      def test_non_numeric_input_rupee_to_dollar(self):
        with self.assertRaises(ValueError):
            rupee_to_dollar('xyz')

      def test_negative_input_rupee_to_dollar(self):
        with self.assertRaises(ValueError):
            rupee_to_dollar(-740)      


if __name__ == '__main__':
    unittest.main()
