import numpy as np
import sys

# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2**1000

print("2**1000 doesn't fit in a 64-bit int. Luckily python 3 int isn't fix precsion")

longpower: int = 2 ** 1000
print("number of bytes of longpower is :", sys.getsizeof(longpower))

sumofdigits: int = sum(int(digit) for digit in str(longpower))

print("longpower =", longpower)
print(f"The sum of the digits is {sumofdigits}")
