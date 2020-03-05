import unittest
"""

To Practice using List, Tuples
Dict and Sets
@eltonaloys

"""


from HW07_Elton_Aloys import anagram_lst, anagrams_dd, anagrams_cntr, covers_alphabet, book_index

class TestAnagrams(unittest.TestCase):
    """ To check for Anagrams """

    def test_anagram_lst(self):
        """ Checking for Anagrams """
        self.assertTrue(anagram_lst("And" , "Dna"))
        self.assertFalse(anagram_lst("test", "Tses"))
        self.assertTrue(anagram_lst("TOMMARVOLORIDDLE", "IAMLORDVOLDEMORT"))
        self.assertTrue(anagram_lst("", ""))

    def test_anagrams_dd(self):
        """ Checking for Anagrams using Dictionary"""
        self.assertEqual(anagrams_dd("listen" , "Silent"), {'l': 0, 'i': 0, 's': 0, 't': 0, 'e': 0, 'n': 0} )
        self.assertEqual(anagrams_dd("Night", "Thing"), {'t': 0, 'h': 0, 'i': 0, 'n': 0, 'g': 0 } )
        self.assertEqual(anagrams_dd("Dusty", "Study"), {'d': 0, 'u': 0, 's': 0, 't': 0, 'y': 0 } )
        self.assertEqual(anagrams_dd("", ""), {} )
    
    def test_anagrams_cntr(self):
        """ Checking for Anagrams using Counter """
        self.assertTrue(anagrams_cntr("Brag", "Grab"))
        self.assertTrue(anagrams_cntr("TheEyes", "TheySee"))
        self.assertTrue(anagrams_cntr("OhLameSaint", "TheMonaLisa"))
        self.assertTrue(anagrams_cntr(" ", " "))

    def test_covers_alphabet(self): 
        """ Checking for Panagram """
        self.assertTrue(covers_alphabet("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(covers_alphabet("The quick brown fox jumps over the lazy dog"))  
        self.assertFalse(covers_alphabet("xyz"))
        self.assertFalse(covers_alphabet(" "))

    def test_book_index(self):
        """ Auto test for Book Index """
        self.assertEqual(book_index([('word1', 1), ('word2', 2), ('word1', 1), ('word1', 3)]), [['word1', [1, 3]], ['word2', [2]]])
        self.assertEqual(book_index([('one', 1)]), [['one', [1]]])
        self.assertEqual(book_index([]), [])


if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)        