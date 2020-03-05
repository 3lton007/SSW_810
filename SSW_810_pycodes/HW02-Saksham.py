"""
    Python program that allows calculations like addition, subtraction, multiplication and division on two fractions
    Author: Saksham Tiwari
"""

class Fraction:
    def __init__(self, numerator, denominator):
        """ Initializes numerator and denominator of newly created fraction object """
        if denominator == 0:
            raise ValueError("Integer cannot be divided by zero")
        elif denominator < 0:
            numerator *= -1
            denominator *= -1

        self.numerator = numerator 
        self.denominator = denominator

    def plus(self, other):
        """ Adds the two fractions after checking if they have same or different denominators and returns a new fraction object as a result """
        if self.denominator == other.denominator:
            result_numerator = self.numerator + other.numerator 
            result_denominator = self.denominator
            print(Fraction(result_numerator, result_denominator))
            return Fraction(result_numerator, result_denominator)
        else:
            result_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            result_denominator = self.denominator * other.denominator
            print(Fraction(result_numerator, result_denominator))
            return Fraction(result_numerator, result_denominator)

    def minus(self, other):
        """ Subtracts the two fractions after checking if they have same or different denominators and returns a new fraction object as a result """
        if self.denominator == other.denominator:
            result_numerator = self.numerator - other.numerator 
            result_denominator = self.denominator
            print(Fraction(result_numerator, result_denominator))
            return Fraction(result_numerator, result_denominator)
        else:
            result.numerator = self.numerator * other.denominator - other.numerator * self.denominator
            result.denominator = self.denominator * other.denominator
            print(Fraction(result_numerator, result_denominator))
            return Fraction(result_numerator, result_denominator)

    def times(self, other):
        """ Multiplies the two fractions and returns a new fraction object as a result """
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        print(Fraction(result_numerator, result_denominator))
        return Fraction(result_numerator, result_denominator)

    def divide(self, other):
        """ Divides the two fractions and returns a new fraction object as a result """
        if other.numerator == 0:
            raise ValueError("Fraction cannot be divided by zero")
        else:
            result_numerator = self.numerator * other.denominator
            result_denominator = self.denominator * other.numerator
            print(Fraction(result_numerator, result_denominator))
            return Fraction(result_numerator, result_denominator)

    def equal(self, other):
        """ Checks if the two fractions are equal and returns a boolean value """
        print(self.numerator * other.denominator == self.denominator * other.numerator)
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __str__(self):
        """ Prints fraction's numerator and denominator """
        return f"{self.numerator}/{self.denominator}"

def main():
    """ Starts the calculator to take in user inputs """
    print("Welcome to the fractions calculator!")

    fraction1_numerator = input("Fraction 1 numerator: ")
    fraction1_denominator = input("Fraction 1 denominator: ")

    fraction2_numerator = input("Fraction 2 numerator: ")
    fraction2_denominator = input("Fraction 2 denominator: ")


    if fraction1_numerator.isdigit() and fraction1_denominator.isdigit() and fraction2_numerator.isdigit() and fraction2_denominator.isdigit():
        fraction1 = Fraction(int(fraction1_numerator), int(fraction1_denominator))
        fraction2 = Fraction(int(fraction2_numerator), int(fraction2_denominator))

        operation = input("Operation (+, -, *, /, ==): ")
        if operation == "+":
            fraction1.plus(fraction2)
        elif operation == "-":
            fraction1.minus(fraction2)
        elif operation == "*":
            fraction1.times(fraction2)
        elif operation == "/":
            fraction1.divide(fraction2)
        elif operation == "==":
            fraction1.equal(fraction2)
        else:
            print("Enter a valid operation (+, -, *, /, ==)")
            main()
    else:
        print("Enter a valid integer")
        main()

main()