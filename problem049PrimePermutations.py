"""Prime permutations
  Show HTML problem content  
Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?"""
from math import sqrt
from itertools import permutations
from typing import List
from utils import isPrime, nextprime


def permutationsofanumber(number: int) -> List[int]:
    listofdigits = [int(i) for i in str(number)[::-1]]
    perms = permutations(listofdigits)
    listnums = [sum(digit * 10 ** i for i, digit in enumerate(list)) for list in perms]
    listnums = list(set(listnums))
    return listnums


def arithmetic_sequences(listofnumbers):
    listofprimes = [number for number in listofnumbers if isPrime(number)]
    prime_permutations = set()

    for i in listofprimes:
        for j in listofprimes:
            if (i - j) + i in listofprimes and 2 * i - j < i < j:
                if "0" not in list(str(j)):
                    prime_permutations.add(((i - j) + i, i, j))

    return prime_permutations


print("The permuation of the digits of 123 is: ", permutationsofanumber(123))
listofperms2 = sorted(permutationsofanumber(1487))
print("Permutations of 1487", listofperms2)
print("The arithmetric sequences including 1487 that are prime:")
print(arithmetic_sequences(listofperms2))


primes = nextprime()
iprime = next(primes)
pm = set()
while iprime <= 10000:
    iprime = next(primes)
    pm = pm.union(arithmetic_sequences(permutationsofanumber(iprime)))


print("The 4-digit arithmetric sequences that are all prime are:")
print(pm)

