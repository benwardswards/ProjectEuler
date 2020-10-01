"""Circular primes

Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?"""
from typing import List, Tuple, Iterator, Generator
from itertools import permutations
from utils import isPrime


def digit_rotations(number: int) -> Iterator[int]:
    digits = [digit for digit in str(number)]
    perms = (int("".join(digits[i:] + digits[:i])) for i in range(len(digits)))
    return perms


print("The digit rotations of 1234 are:")
print(list(digit_rotations(1234)))
print("The digit rotations of 12311 are:")
print(list(digit_rotations(12311)))


def nextprime() -> Iterator[int]:
    number: int = 2
    while True:
        if isPrime(number):
            yield number
        number += 1


def isCircularPrime(number: int) -> bool:
    for i in digit_rotations(number):
        if not isPrime(i):
            return False
    return True


assert isCircularPrime(1) == False
assert isCircularPrime(2) == True
assert isCircularPrime(19937) == True
assert isCircularPrime(23) == False


primes: Iterator[int] = nextprime()
iprime: int = next(primes)
count: int = 0
while iprime <= 1_000_000:
    if isCircularPrime(iprime):
        count += 1
    iprime = next(primes)

print(f"The number of circular primes is {count}")

