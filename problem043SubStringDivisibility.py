"""The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import combinations
from itertools import permutations
from functools import reduce
from math import sqrt
from utils import isPrime
from typing import List, Tuple

assert isPrime(3) == True
assert isPrime(10) == False

listofdigits: str = "1234567890"
numberofdigits: int = 10
digits: List[str] = list("1234567890")

substringdigits: List[int] = [
    int(digits[i] + digits[i + 1] + digits[i + 2])
    for i, digit in enumerate(digits)
    if i > 0 and i <= 7
]
print("substrings of 0123456789:", substringdigits)

listofPrimes: List[int] = [2, 3, 5, 7, 11, 13, 17]


def pandigital_substring_divisor(in_digits: Tuple[str, ...]) -> bool:
    substringdigits: List[int] = [
        int(in_digits[i] + in_digits[i + 1] + in_digits[i + 2])
        for i, _ in enumerate(in_digits)
        if 0 < i <= 7
    ]
    return 0 == sum(N % D for N, D in zip(substringdigits, listofPrimes))


list_pandigital_st_div: List[int] = []
for l_digits in permutations(listofdigits):
    if pandigital_substring_divisor(l_digits):
        list_pandigital_st_div.append(int("".join(l_digits)))

print(list_pandigital_st_div)
print(
    "The sum of the pandigital substring prime divisors is:",
    sum(list_pandigital_st_div),
)
