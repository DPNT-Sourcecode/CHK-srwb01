from solutions.SUM import sum_solution

from unittest import TestCase


class TestSum(TestCase):

    def test_sum(self):
        """ vanilla case """
        self.assertEqual(sum_solution.compute(1, 2), 3)

    def test_out_of_bounds_s1_s2(self):
        """ both smaller than bounds """
        with self.assertRaises(ValueError):
            sum_solution.compute(-1, -1)

    def test_out_of_bounds_s1(self):
        """ first smaller than bounds """
        with self.assertRaises(ValueError):
            sum_solution.compute(-1, 2)

    def test_out_of_bounds_s2(self):
        """ second smaller than bounds """
        with self.assertRaises(ValueError):
            sum_solution.compute(2, -1)

    def test_out_of_bounds_b1_b2(self):
        """ both bigger than bounds """
        with self.assertRaises(ValueError):
            sum_solution.compute(101, 101)

    def test_out_of_bounds_b1(self):
        """ first bigger than bounds """
        with self.assertRaises(ValueError):
            sum_solution.compute(101, 1)

    def test_out_of_bounds_b2(self):
        """ second bigger than bounds """
        with self.assertRaises(ValueError):
            sum_solution.compute(1, 101)
