"""

Learning Python List Functions
@eltonaloys

"""

import unittest
from HW06_Elton_Aloys import list_copy, list_difference, list_intersect, remove_vowels, check_pwd, insertion_sort

class TestList(unittest.TestCase):
    """ Class containing test_cases for functions list_copy, list_intersect, list_difference , remove_vowels , check_pwd , insertion sort """

    def test_list_copy(self):
        """ TO test if copy of a list works """
        self.assertEqual(list_copy([4,6,7]), [4,6,7])
        self.assertEqual(list_copy([]), [])

    def test_list_intersect(self):
        """ To test if list_intersect works properly """
        self.assertEqual(list_intersect([1,2,3], [2]), [2])
        self.assertEqual(list_intersect([4,5,6] , [7,8,9]), [])
        self.assertEqual(list_intersect([], []) , [])

    def test_list_difference(self):
        """ to test list_difference works properly """
        self.assertEqual(list_difference([8,9,10], [9]), [8,10])
        self.assertEqual(list_difference([8,9,10], [1]), [8,9,10])
        self.assertEqual(list_difference([], []) , [])

    def test_remove_vowels(self):
        """ Function to tests if fuction remove_vowels works properly """
        self.assertEqual(remove_vowels("bcde") , "bcd")
        self.assertEqual(remove_vowels("lmn"), "lmn")
        self.assertEqual(remove_vowels(""), "")

    def test_check_pwd(self):
        """ Function to test check_pwd works """
        self.assertTrue(check_pwd("Garo66f6")) 
        self.assertFalse(check_pwd("xyz"))
        self.assertFalse(check_pwd(""))

    def test_insertion_sort(self):
        """ Function that tests insertion_sort works properly """
        self.assertEqual(insertion_sort([4, 3, 2, 1]), [1, 2, 3, 4])
        self.assertEqual(insertion_sort([2, 3, 4, 1, 4, 2, 4]), [1, 2, 2, 3, 4, 4, 4])
        self.assertEqual(insertion_sort([]) , [])

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)