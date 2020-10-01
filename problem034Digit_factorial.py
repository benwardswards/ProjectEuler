"""Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
from math import factorial

assert factorial(5) == 120
print(f"9! = {factorial(9)}")

# Figure out the max possible curious number:
print([10 ** i for i in range(1, 10) if factorial(9) * i > 10 ** i])


def factorial_digit_sum(num: int) -> int:
    return sum(factorial(int(i)) for i in str(num))


assert factorial_digit_sum(1234) == 1 + factorial(2) + factorial(3) + factorial(4)

sum_of_curious = sum(i for i in range(9, 1000000) if i == factorial_digit_sum(i))

print("The sum of all curious numbers is:", sum_of_curious)

