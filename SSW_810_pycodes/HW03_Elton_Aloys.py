"""

@eltonaloys

Script for running and testing
the Fraction Calcualtor

"""

import unittest

class Fraction:
    def __init__(self,num,denom):    
        """Initializing numerator and denominator of  created fraction object"""
        self.num = num
        self.denom = denom
        if self.denom == 0:
            raise ValueError ("Interger cannot be divided by zero")
        elif self.denom < 0:
             print("Denom is negative")
             self.denom = -1*self.denom
             self.num = -1*self.num             

    def __str__(self):                       
        """Prints Fractions Numerator and Denominator"""
        return f"{self.num}/{self.denom}"

    def __add__(self,other):                    
        """Adds two fractions and creates a new fraction object as result"""

        top_plus = self.num * other.denom + other.num * self.denom
        bottom_plus = self.denom * other.denom
        return Fraction(top_plus,bottom_plus)
         

    def __sub__(self,other):                   
        """Subtracts two fractions and creates a new fraction object as result"""
        top_minus = self.num * other.denom - other.num * self.denom    
        bottom_minus = self.num * other.denom
        return Fraction(top_minus,bottom_minus)

    def __mul__(self,other):                   
        """Multiplies two fractions and creates a new fraction object as result"""
        top_times = self.num * other.num
        bottom_times = self.denom * other.denom 
        return Fraction(top_times,bottom_times)

    def __truediv__(self,other):                  
        """Divides two fraction and creates a new fraction object as result"""
        top_divide = self.num * other.denom
        bottom_divide = self.denom * other.num
        return Fraction(top_divide,bottom_divide)

    def __eq__(self,other):                     
        """Compares two fraction and returns True if its equal to second fraction"""
        return self.num * other.denom == other.num * self.denom
           
    def __ne__(self,other):                     
        """Compares two fraction and returns True if its notequal to second fraction"""
        return self.num * other.denom != other.num * self.denom

    def __lt__(self,other):                     
        """Compares two fraction and returns True if its lessthan to second fraction"""
        return self.num * other.denom < other.num * self.denom

    def __le__(self,other):                     
        """Compares two fraction and returns True if its less than or equal to second fraction"""
        return self.num * other.denom <= other.num * self.denom

    def __gt__(self,other):                     
        """Compares two fraction and returns True if its greater than to second fraction"""
        return self.num * other.denom > other.num * self.denom

    def __ge__(self,other):                     
        """Compares two fraction and returns True if its greater than equal to second fraction""" 
        return self.num * other.denom >= other.num * self.denom


    def test_suit():
        """Running mannual test cases to check the code's efficiency"""
        print*("Test_Suite RUnning")
        f12 = Fraction(1,2)
        f44 = Fraction(4,4)
        f128 = Fraction(12,8)
        f32 = Fracttion(3,2)

        print(f"{f12} + {f12} = {f12.__add__(f12)} [4/4]")
        print(f"{f44} - {f12} = {f44.__sub__(f12)} [4/8]")
        print(f"{f12} + {f44} = {f12.__add__(f44)} [12/8]")
        print(f"{f128} == {32} is {f128.__eq__(f32)} [True]")



def main():
    print("Welcome to Fraction Calculator")   
    """Taking Input from user for the Fraction"""        

    try:
        f1_num = int(input("Fraction 1 numerator:"))            
        f1_denom = int(input("Fraction 1 denominator:"))

        f2_num = int(input("Fraction 2 numerator:"))
        f2_denom = int(input("Fraction 2 denominator:"))

    except ValueError:
        print("Give a valid Interger")
        main()

    f1 = Fraction(f1_num,f1_denom)
    f2 = Fraction(f2_num,f2_denom)


    
    ops = input("Enter Operation [+,-,*,/,==,!=,<,<=,>,>=]:")      
    if ops == "+":
        plus = f1 + f2
        print(f" The current result is: {plus}")
    elif ops == "-":
        minus = f1 - f2 
        print(f" The current result is: {minus}")
    elif ops == "*":
        times = f1 * f2
        print(f" The current result is: {times}")
    elif ops == "/":
        divide = f1 / f2
        print(f" The current result is: {divide}")
        
        
    elif ops == "==":
        equal = f1 == f2
        print(f" The Current result is: {equal}")
    elif ops == "!=":
        notequal = f1 != f2
        print(f" The current result is: {notequal}")
    elif ops == "<":
        lessthan = f1 < f2
        print(f" The Current result is: {lessthan}")
    elif ops == "<=":
        lessthaneql = f1 <= f2
        print(f" The Current result is: {lessthaneql}")
    elif ops == ">":
        greaterthan = f1 > f2
        print(f" The Current result is: {greaterthan}")
    elif ops == ">=":
        greaterthaneql = f1 >= f2
        print(f" The Current result is: {greaterthaneql}")     


    else:                          

        main()  
            
main()    

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
        self.assertEqual(str(Fraction(1, 2) - Fraction(1, 2)), "0/2")

    def test_mul(self):
        """checks if __mul()__ functions returns correct result"""
        self.assertEqual(str(Fraction(1, 2) * Fraction(1, 2)), "1/4")

    def test_div(self):
        """checks if __div()__ functions returns correct result"""
        self.assertEqual(str(Fraction(1, 2) / Fraction(1, 2)), "2/2")

    def test_eql(self):
        """checks if __eql()__ functions returns correct results"""
        self.assertTrue(Fraction(1, 2) == Fraction(1, 2))

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

    
if __name__ == '__main__':
    #test_suite()
    unittest.main(exit = False, verbosity = 2)
    #main()