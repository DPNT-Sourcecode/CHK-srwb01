from solutions.CHK import checkout

from unittest import TestCase


class TestSum(TestCase):

    def test_chkE(self):
        self.assertEqual(checkout('BBE'), 85)

