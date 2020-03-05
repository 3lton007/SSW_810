import unittest
"""
Practicing Iteration,Lists,Ranges and Strings
@elton_aloys

"""
from HW04_Elton_Aloys import Fraction, count_vowel, last_occurance, my_enumerate

class TestFraction(unittest.TestCase):
    """Running Few Test cases Automatically"""
    def test_init(self):
        frac = Fraction(1, 2)
        self.assertEqual(frac.num, 1)
        self.assertEqual(frac.denom, 2)

    def test_add(self):
        """checks if __add()__ functions returns correct result"""
        self.assertEqual(str(Fraction(1, 2) + Fraction(1, 2)), "4/4")

    def test_sub(self):
        """checks if __sub()__ functions returns correct result"""
        self.assertEqual(str(Fraction(1, 2) - Fraction(1, 2)), "0/4")

    def test_mul(self):
        """checks if __mul()__ functions returns correct result"""
        self.assertEqual(str(Fraction(1, 2) * Fraction(-1, 2)), "-1/4")

    def test_div(self):
        """checks if __div()__ functions returns correct result"""
        self.assertEqual(str(Fraction(1, 2) / Fraction(1, 2)), "2/2")

    def test_eql(self):
        """checks if __eql()__ functions returns correct results"""
        self.assertTrue(Fraction(-4, 2) == Fraction(-4, 2))

    def test_noteql(self):
        """checks if __noteql()__ functions returns correct results"""
        self.assertTrue(Fraction(1, 2) != Fraction(1, 3))

    def test_lessthan(self):
        """checks if __lessthan()__ functions returns correct results"""
        self.assertTrue(Fraction(1, 2) < Fraction(3, 2))

    def test_lessthaneql(self):
        """checks if __lessthaneql()__ functions returns correct results"""
        self.assertTrue(Fraction(1, 2) <= Fraction(1, 2))

    def test_greaterthan(self):
        """checks if __greaterthan()__ functions returns correct results"""
        self.assertTrue(Fraction(3, 2) > Fraction(1, 2))

    def test_greaterthaneql(self):
        """checks if __greaterthaneql()__ functions returns correct results"""
        self.assertTrue(Fraction(1, 2) >= Fraction(1, 2))

    def test_str(self):
        """checks if __str()__ functions returns correct results"""
        self.assertEqual(str(Fraction(1, 2)), "1/2")  

    def test_simplify(self):
        """simplifies fraction"""
        self.assertEqual(Fraction(-3,9).simplify(), Fraction(-1,3).simplify())        

class TestIteration(unittest.TestCase):
    def test_count_vowel(self):
        """to check for vowel count"""
        self.assertEqual(count_vowel('Itachi Uchiha'), 6)
        self.assertEqual(count_vowel('Susanno'), 3)
        self.assertEqual(count_vowel('Madara'), 3)

    def test_last_occurance(self):
        """to check for last occurence"""
        self.assertEqual((last_occurance("o","python")), 4)
        self.assertEqual((last_occurance("l","elton")), 1)
        self.assertEqual((last_occurance("t","tiger")), 0)    

    def test_my_enumerate(self):
        """checking for offset and value"""
        self.assertEqual(list(my_enumerate("abc")), list(enumerate("abc")))

if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)
      

    