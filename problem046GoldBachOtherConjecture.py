"""Goldbach's other conjecture
  Show HTML problem content  
Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from math import sqrt
from itertools import product
from utils import isPrime, nextprime
from typing import List, Iterator, Set


def odd_composites():
    # numbers that are not prime and not 1
    count: int = 1
    while True:
        count += 2  # is odd
        if not isPrime(count):
            yield count


comps: Iterator[int] = odd_composites()


primes: Iterator[int] = nextprime()

listofprimes: List[int] = [next(primes) for i in range(1500)]
listofsqaures: List[int] = [2 * i ** 2 for i in range(300)]
print("max prime", listofprimes[-1], "max sqare", listofsqaures[-1])

prime_plus_double_square: Set[int] = {
    i + j for i, j in product(listofprimes, listofsqaures)
}

while True:

    firstnonGoldbach: int = next(comps)
    if firstnonGoldbach > listofprimes[-1] + listofsqaures[1]:
        assert False, "not enough primes"
    if firstnonGoldbach > listofprimes[1] + listofsqaures[-1]:
        assert False, "not enough compostites"

    if firstnonGoldbach not in prime_plus_double_square:
        print("first non Goldbach odd composite is", firstnonGoldbach)
        break

