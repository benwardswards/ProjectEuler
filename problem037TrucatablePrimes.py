"""Truncatable primes

Problem 37
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from math import sqrt
from itertools import permutations
from typing import List
from utils import isPrime, nextprime

assert isPrime(1) == False
assert isPrime(0) == False
assert isPrime(7)


def listToNumber(numList: List[int]) -> int:
    s = "".join([str(i) for i in numList])
    return int(s)


assert listToNumber([1, 2, 3, 4]) == 1234


def numberToList(number: int) -> List[int]:
    return [int(digit) for digit in str(number)]


assert numberToList(1234) == [1, 2, 3, 4]


def isTrucatablePrimes(number: int) -> bool:
    # print(number)
    listofdigits: List[int] = numberToList(number)
    # print(listofdigits)
    lenList: int = len(listofdigits)

    # truncatable from left
    for i in range(lenList):
        # print(listofdigits[i:lenList])
        if not isPrime(listToNumber(listofdigits[i:lenList])):
            # print(listofdigits[i:lenList])
            return False

    # truncatable from right
    for i in range(lenList):
        # print(listofdigits[0:(i+1)])
        if not isPrime(listToNumber(listofdigits[0 : (i + 1)])):
            # print(listofdigits[0:(i+1)])
            return False

    return True


assert isTrucatablePrimes(3797) == True
assert isTrucatablePrimes(37) == True
assert isTrucatablePrimes(71) == False
assert isTrucatablePrimes(35) == False
assert isTrucatablePrimes(13) == False

primes = nextprime()
listofTrucatablePrimes: List[int] = []
while len(listofTrucatablePrimes) <= 10:
    prime = next(primes)
    if isTrucatablePrimes(prime) and prime > 9:
        listofTrucatablePrimes.append(prime)


print(listofTrucatablePrimes)
print("The sum of truncable primes is: ", sum(listofTrucatablePrimes))
