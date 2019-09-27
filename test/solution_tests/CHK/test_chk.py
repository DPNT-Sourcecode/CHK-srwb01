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

    def test_chk2F(self):
        self.assertEqual(checkout_solution.checkout('FF'), 20)

    def test_chk3F(self):
        self.assertEqual(checkout_solution.checkout('FFF'), 20)

    def test_chk4F(self):
        self.assertEqual(checkout_solution.checkout('FFFF'), 30)

    def test_chk5F(self):
        self.assertEqual(checkout_solution.checkout('FFFFF'), 40)

    def test_chkSTX(self):
        self.assertEqual(checkout_solution.checkout('STX'), 45)

    def test_chkST2X(self):
        self.assertEqual(checkout_solution.checkout('STXX'), 65)

    def test_chk3SZ(self):
        self.assertEqual(checkout_solution.checkout('SSSZ'), 65)

    def test_chk3ZS(self):
        self.assertEqual(checkout_solution.checkout('ZZZS'), 65)

    def test_chkSTXS(self):
        self.assertEqual(checkout_solution.checkout('STXS'), 62)


