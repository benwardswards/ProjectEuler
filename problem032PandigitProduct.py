"""Pandigital products:  Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from itertools import permutations, product
from typing import Set, Tuple, List


def Number(numList: List[int]) -> int:
    return sum(digit * (10 ** (i)) for i, digit in enumerate(numList[::-1]))


def Number2(numList: List[int]) -> int:
    return int("".join(str(digit) for digit in numList))


assert Number([1]) == 1
assert Number([1, 2, 3]) == 123


def prod_of_pan_digits(perm: List[int]) -> Set[int]:
    products: Set[int] = set()
    for i in range(1, 9):
        for j in range(i + 1, 9):
            first = Number2(perm[0:i])
            second = Number2(perm[i:j])
            product_ = Number2(perm[j:10])
            if first * second == product_:
                products.add(product_)
                print(products)
    return products


print("starting to count")
set_of_pandigit: Set[int] = set()

for permutation in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]):
    set_of_pandigit.update(prod_of_pan_digits(list(permutation)))

print(f"The products that are pan digit are")
print(set_of_pandigit)

print("The sum is ", sum(set_of_pandigit))

