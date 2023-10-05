import sys
sys.path.insert(0, "../../src/")  # noqa
import my_utils
import random
import unittest
import numpy as np


class TestMyUtils(unittest.TestCase):
    def test_mean_basic(self):
        # Does mean of random ints match numpy's built-in mean function?
        for i in range(100):
            randomlist = random.sample(range(-50, 50), 5)
            r = my_utils.find_mean(randomlist)
            self.assertEqual(np.mean(randomlist), r)

    def test_mean_lenarray(self):
        # If input array is empty, is a correct error returned?
        self.assertRaises(ValueError, my_utils.find_mean, [])

    def test_mean_arrayvals(self):
        # If input array contains non-ints, is the correct error returned?
        self.assertRaises(TypeError, my_utils.find_mean, ["test", np.pi])

    def test_median_basic(self):
        # Does median of random ints match numpy's built-in median function?
        for i in range(100):
            randomlist = random.sample(range(-50, 50), 5)
            r = my_utils.find_median(randomlist)
            self.assertEqual(np.median(randomlist), r)

    def test_median_lenarray(self):
        # If the input array is empty, is a correct error returned?
        self.assertRaises(ValueError, my_utils.find_median, [])

    def test_std_basic(self):
        # Does std of random ints match numpy's built-in std function?
        for i in range(100):
            randomlist = random.sample(range(-50, 50), 5)
            r = my_utils.find_std(randomlist)
            self.assertEqual(np.round(np.std(randomlist), 2), np.round(r, 2))

    def test_std_lenarray(self):
        # If the input array is empty, is a correct error returned?
        self.assertRaises(ValueError, my_utils.find_std, [])

    def test_std_arrayvals(self):
        # If input array contained non-ints, is the correct error returned?
        self.assertRaises(TypeError, my_utils.find_std, ["test", 1.2])

    def test_get_column_valueerror(self):
        # If ValueError is raised does handled exception correctly return None?
        get_col_result = my_utils.get_column("test_data.csv", 0, "Chile", 0)
        self.assertIsNone(get_col_result)

    def test_get_column_nofile(self):
        # Is FileNotFoundError raised correctly when wrong file name is given?
        self.assertRaises(FileNotFoundError, my_utils.get_column,
                          "test.csv", 0, "Chile", 0)
