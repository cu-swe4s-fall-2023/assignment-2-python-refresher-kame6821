import sys
sys.path.insert(0, "../src/")  # noqa
import my_utils
import random
import unittest

#print(my_utils.find_mean([]))
#print("int" == type(2.3))

class TestMyUtils(unittest.TestCase):
    def test_mean_basic(self):
        for i in range(100):
            randomlist = random.sample(range(-50, 50), 5)
            r = my_utils.find_mean(randomlist)
            self.assertEqual(sum(randomlist)/len(randomlist), r)

    def test_mean_lenarray(self):
        self.assertRaises(ZeroDivisionError, my_utils.find_mean, [])
        
    def test_mean_arrayvals(self):
        self.assertRaises(TypeError, my_utils.find_mean, ["test", 1.2])

    def test_median_basic(self):
        for i in range(100):
            randomlist = random.sample(range(-50, 50), 5)
            r = my_utils.find_median(randomlist)
            self.assertEqual((len(randomlist)+1)/2, r)
            
    def test_median_lenarray(self):
        self.assertRaises(ValueError, my_utils.find_median, [])

    def test_std_basic(self):
        for i in range(100):
            randomlist = random.sample(range(-50, 50), 5)
            r = my_utils.find_std(randomlist)
            randomlist_mean = sum(randomlist)/len(randomlist)
            numerator = sum((value - randomlist_mean) ** 2 for value in randomlist)
            self.assertEqual(numerator/len(randomlist), r)

    def test_std_lenarray(self):
        self.assertRaises(ZeroDivisionError, my_utils.find_std, [])
        
    def test_std_arrayvals(self):
        self.assertRaises(TypeError, my_utils.find_std, ["test", 1.2])
        
    #def setUp(self):
        #self.test_file_name = "setup_test_file.txt"
        #f = open(self.test_file_name, "w")
        #self.direct_sum

    def test_get_column_error(self):
        self.assertRaises(ValueError, my_utils.get_column, 
                          "../data/Agrofood_co2_emission.csv", 0, "Zimbabwe", 0)
    

    