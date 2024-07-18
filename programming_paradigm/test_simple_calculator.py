import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    # Setting up SimpleCalculator before each test
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(2,3),5)
        self.assertEqual(self.calc.add(-1,1),0)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3,2),1)
        self.assertEqual(self.calc.subtract(2,3),2-3)
   
    def test_division(self):
        self.assertEqual(self.calc.divide(4,2),2)
        self.assertIsNone(self.calc.divide(1,0))
   
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2,2),4)
        self.assertEqual(self.calc.multiply(-2,-2),(-2)*(-2))


if __name__ == "__main__":
  unittest.main()
        
