from math import gcd, lcm


class Rational:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int):
            raise TypeError("The entered value is of the wrong type")
        if not denominator:
            raise ValueError("Cannot be divided by zero")

        self.__numerator = numerator
        self.__denominator = denominator

    def fraction_reduction(self):
        greatest_common_divisor = gcd(self.__numerator, self.__denominator)
        if greatest_common_divisor:
            return int(self.__numerator / greatest_common_divisor), int(
                self.__denominator / greatest_common_divisor)

    def result(self):
        return self.__numerator / self.__denominator

    def multiplication(self, new_numerator, new_denominator):
        self.__numerator = self.__numerator * new_numerator
        self.__denominator = self.__denominator * new_denominator

    def division(self, new_numerator, new_denominator):
        self.__numerator = int(self.__numerator / new_numerator)
        self.__denominator = int(self.__denominator / new_denominator)

    def sum(self, new_numerator, new_denominator):
        lcm_denominator = lcm(self.__denominator, new_denominator)
        first_numerator = lcm_denominator / self.__denominator * self.__numerator
        second_numerator = lcm_denominator / new_denominator * new_numerator
        self.__numerator = int(first_numerator + second_numerator)
        self.__denominator = lcm_denominator

    def minus(self, new_numerator, new_denominator):
        lcm_denominator = lcm(self.__denominator, new_denominator)
        first_numerator = lcm_denominator / self.__denominator * self.__numerator
        second_numerator = lcm_denominator / new_denominator * new_numerator
        self.__numerator = int(first_numerator - second_numerator)
        self.__denominator = lcm_denominator


rational = Rational(2, 6)
rational.multiplication(4, 6)
result = "/".join(map(str, rational.fraction_reduction()))
print(f"Simple fraction: {result}")
print(f"In decimal: {rational.result()}")