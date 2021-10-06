from math import gcd


class Rational:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError("The entered value is of the wrong type")
        if not denominator:
            raise ValueError("Cannot be divided by zero")

        self.__numerator = numerator
        self.__denominator = denominator

        hcf = gcd(self.__numerator, self.__denominator)
        if hcf:
            self.__numerator /= hcf
            self.__denominator /= hcf

    def reduction(self):
        return f"{int(self.__numerator)}/{int(self.__denominator)}"

    def result(self):
        return self.__numerator / self.__denominator


rational = Rational(2, 6)
print(rational.reduction())
print(rational.result())
