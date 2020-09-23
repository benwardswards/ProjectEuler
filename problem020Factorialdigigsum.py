"""Factorial digit sum  
Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""
from functools import reduce

# 100 factorail not in int64

number: int = reduce((lambda x, y: x * y), range(1, 101))
print("100 factorial = ", number)

sumofdigits: int = sum(int(digit) for digit in str(number))
print(f"The sum of the digits of 100 factorail is {sumofdigits}")
