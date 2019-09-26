from solutions.CHK import checkout_solution

from unittest import TestCase


class TestSum(TestCase):

    def test_chkE(self):
        self.assertEqual(checkout_solution.checkout('BBE'), 85)

    def test_chkEE(self):
        self.assertEqual(checkout_solution.checkout('BBEE'), 110)



