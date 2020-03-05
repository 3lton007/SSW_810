import unittest

"""
TestCases for ReverseString , ReverseEnumerate , SecondOccurance
@eltonaloys

"""

from HW05_Elton_Aloys import reverse, rev_enumerate, find_second, get_lines

class Test(unittest.TestCase):
    def test_rev_string(self):
        """ to check reverse of a string"""
        self.assertEqual(reverse("hi"),"ih")
        self.assertEqual(reverse("olleh"),"hello")
        self.assertEqual(reverse("dante"),"etnad")

    def test_rev_enumerate(self):
        """to check for reverse enumerate functioning"""
        self.assertEqual(list(rev_enumerate("abc")) , [(2, "c"), (1,"b"), (0,"a")])
        self.assertEqual(list(rev_enumerate("dbcd")) , [(3,"d"),(2, "c"), (1,"b"), (0,"d")])
        self.assertEqual(list(rev_enumerate("")) , [])

    def test_find_second(self):
        """to check for second occurance"""
        self.assertEqual((find_second("ab","abcdeabc")), 5)
        self.assertEqual((find_second("bc","abcdeabc")), 6)
        self.assertEqual((find_second("ge","fedegefege")), 8)
         
    def test_get_lines(self):
        """ Checking for Get_lines functioning properly"""
        path = '/Users/jrr/Downloads/hw05.txt'
        expect = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>','<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines(path))
        self.assertEqual(expect,result)
        




if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)