"""Digit Cancelling Fractions

"""
from itertools import product
from typing import List, Tuple
from fractions import Fraction
from pprint import pprint


def reducedform(num: int, denom: int) -> List[int]:
    pass


def safe_div(x: int, y: int) -> float:
    if y == 0:
        return -1
    return x / y


cancelling_fractions: List[Tuple[int, int]] = []

for fn, sn, fd, sd in product(range(10), range(10), range(10), range(10)):
    num: int = 10 * fn + sn
    denom: int = 10 * fd + sd
    if num < denom:
        if denom != 0 and fn != sn:
            if fn == sd and num / denom == safe_div(sn, fd):
                cancelling_fractions.append((num, denom))
                # print(num, denom)

            if sn == fd and num / denom == safe_div(fn, sd):
                cancelling_fractions.append((num, denom))
                # print(num, denom)


prod = Fraction(1)
for frac in cancelling_fractions:
    print(frac, " in reduced form is:", Fraction(*frac))
for frac in cancelling_fractions:
    prod *= Fraction(*frac)

print("The product of the fractions is:")
print(prod)

