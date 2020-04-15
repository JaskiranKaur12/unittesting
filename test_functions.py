from unittest import TestCase
from functions import divide,multiply

class TestFunctions(TestCase):
    def test_divide_result(self):
        dividend=20
        divisor=5
        expected_result=4.0
        self.assertAlmostEqual(divide(dividend,divisor),expected_result,delta=0.00001)#delta allows us to equate to almost difference

    def test_divide_negative(self):
        dividend = -20
        divisor = 5
        expected_result = -4.0
        self.assertAlmostEqual(divide(dividend,divisor),expected_result,delta=0.00001)

    def test_divide_zero(self):
        dividend = 0
        divisor = 5
        expected_result = 0
        self.assertEqual(divide(dividend,divisor),expected_result)

    def test_for_error_divide_0(self):
        #self.assertRaises(ValueError,lambda: divide(25,0))
        with self.assertRaises(ValueError):
               divide(25,0)

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()

    def test_multiply_single_value(self):
        expected=15
        self.assertEqual(multiply(expected),expected)

    def test_multiply_zero(self):
        expected=0
        self.assertEqual(multiply(expected),expected)

    def test_multiply_result(self):
        input=(3,6)
        expected=18
        self.assertEqual(multiply(*input),expected)

    def test_multiply_results_with_zero(self):
        inputs = (3,5,0)
        expected = 0
        self.assertEqual(multiply(*inputs),expected)

    def test_multiply_negative(self):
        inputs = (3,-5,2)
        expected = -30
        self.assertEqual(multiply(*inputs),expected)

    def test_multiply_floats(self):
        inputs = (3.0,2)
        expected = 6.0
        self.assertEqual(multiply(*inputs),expected)

gdfgvccccccccc