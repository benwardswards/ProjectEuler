"""
Champernowne's constant

Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
from typing import Iterator


def list_of_digit() -> Iterator[int]:
    """ yields the digits from counting from 1,
    1,2,3,4,5,6,7,8,9,(1,0),(1,1),(1,2)....
    """
    number: int = 0
    while True:
        number += 1
        for digits in str(number):
            yield int(digits)


gendigits = list_of_digit()

prod: int = 1
for i in range(1, 1000001):
    output = next(gendigits)
    if (
        i == 1
        or i == 10
        or i == 100
        or i == 1000
        or i == 10000
        or i == 100000
        or i == 1000000
    ):
        prod *= output
        print(i, output)

print("The product of the digits in the expansion is ", prod)

