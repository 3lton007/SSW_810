import unittest
"""
Practicing Iteration,Lists,Ranges and Strings
@eltonaloys

"""

#>>>>>>>>> PART 1 <<<<<<<<<

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
        bottom_minus = self.denom * other.denom
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

    def simplify(self):
        gcf = min(self.num, self.denom)

        while gcf > 1:
            if (self.num % gcf == 0) and (self.denom % gcf == 0):
                return Fraction(int(self.num/gcf), int(self.denom/gcf))
                break
            else:
                gcf = gcf - 1
        else:
            return Fraction(self.num, self.denom)


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

#>>>>>> PART 3 <<<<<<<<<<<<

def count_vowel(str):
    """ Count Vowels in a string"""
    count = 0
    vowel = "aeiouAEIOU"
    for char in str:
        if  char in vowel:
            count = count + 1
    return count


#>>>>>>> PART 2 <<<<<<<<<

def last_occurance(target, my_list):
    """ Finding the index of target """
    for index, c in enumerate(my_list):
        if target == c:
            return index



#>>>>>>>> PART 4 <<<<<<<<<

def my_enumerate(sequence):
  """ Creating own my_enumerate function    """ 
  for i in range(len(sequence)):
      yield i, sequence[i]


fraction = Fraction(3, 9)

print(fraction.simplify())