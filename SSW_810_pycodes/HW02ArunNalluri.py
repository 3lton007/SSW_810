class Fraction:
    """Class Fraction creates and stores variables while also doing operations with fractions"""
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator
    def __str__(self):
        return(f"{self.numerator}/{self.denominator}")
    
    def plus(self,other):
        
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        resultnumerator = self.numerator+other.numerator
        resultdenominator = self.denominator*other.denominator 
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def minus(self,other):
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        resultnumerator = self.numerator-other.numerator
        resultdenominator = self.denominator*other.denominator 
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def times(self,other):
        if(self.denominator*other.denominator<0):
            resultnumerator = -1*self.numerator*other.numerator
            resultdenominator = abs(self.denominator*other.denominator) 
        else:
            resultnumerator = self.numerator*other.numerator
            resultdenominator = self.denominator*other.denominator 
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def divide(self,other):
        resultnumerator = self.numerator*other.denominator
        resultdenominator = self.denominator*other.numerator
        newvalues = (resultnumerator,resultdenominator)
        return newvalues

    def equal(self,other):
        self.numerator=self.numerator*other.denominator
        other.numerator=self.denominator*other.numerator
        if(self.numerator==other.numerator):
            print("first and 2nd fractions provided are equal")    
        else:
            print("first and 2nd fractions provided are not equal")
        return

def main():
    """Main function takes in two fractions and operation and then calls the appropriate function"""
    print("Welcome to the fraction calculator!")
    try:
        num = int(input("Fraction 1 numerator: "))
        den = int(input("Fraction 1 denominator: "))
    except ValueError:
        print('please enter only an integer')
        num = int(input("Fraction 1 numerator: "))
        den = int(input("Fraction 1 denominator: "))
    
    fraction1 = Fraction(num,den)
    operation = input("Please enter desired operation (+,-,*,/,==) or any other key to exit the program: ")
    while operation in ['+','-','*','/','==']:
        try:                                        
            num2 = int(input("Fraction 2 numerator: "))
            den2 = int(input("Fraction 2 denominator: "))
        except ValueError:
            print('please enter only an integer')
            num = int(input("Fraction 1 numerator: "))
            den = int(input("Fraction 1 denominator: "))

        fraction2 = Fraction(num2,den2)
        if(operation=="+"):
            newvalues = fraction1.plus(fraction2)
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="-"):
            newvalues = fraction1.minus(fraction2)
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="*"):
            newvalues = fraction1.times(fraction2)
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="/"):
            newvalues = fraction1.divide(fraction2)
            fraction1 = Fraction(newvalues[0],newvalues[1])
            print(f"The current result is: {fraction1}")
        elif(operation=="=="):
            fraction1.equal(fraction2)
        operation = input("Please enter your next operation (+,-,*,/,==) or any other key to exit the program:  ")

    print(f"So your final result was:  {fraction1}")
    print("Thank you for trying my program have a nice day!")

main()