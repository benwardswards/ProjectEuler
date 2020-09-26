"""Lexicographic permutations
  
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

from itertools import permutations
from typing import List
import sys

# check permuations goes in the correct order
print(list(permutations(list("012"))))

list_of_permutations: List[str] = list(permutations(list("0123456789")))
print(sys.getsizeof(list_of_permutations), "Bytes long")

print("The first 10 permutations in order")
for p in list_of_permutations[:10]:
    print(p)

listdigitsperm1000000 = list_of_permutations[999999]
perm1000000 = "".join(digit for digit in listdigitsperm1000000)

print(f"The millionth permutation is {perm1000000}")

