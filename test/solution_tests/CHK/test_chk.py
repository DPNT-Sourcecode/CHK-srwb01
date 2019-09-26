from solutions.CHK import checkout_solution

from unittest import TestCase


class TestSum(TestCase):

    def test_chkE(self):
        self.assertEqual(checkout_solution.checkout('BBE'), 85)

    def test_chkEE(self):
        self.assertEqual(checkout_solution.checkout('BBEE'), 110)

    def test_chkABCDE(self):
        self.assertEqual(checkout_solution.checkout('ABCDE'), 155)

    def test_chk5A(self):
        self.assertEqual(checkout_solution.checkout('AAAAA'), 200)

    def test_chk6A(self):
        self.assertEqual(checkout_solution.checkout('AAAAAA'), 250)

