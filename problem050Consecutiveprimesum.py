"""Consecutive prime sum

Problem 50
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from typing import List
from utils import isPrime, nextprime

primes = nextprime()
primes_below12000 = [next(primes) for _ in range(1000)]

maxlength = 0
maxprime = -1
for prime_min in range(len(primes_below12000)):
    for prime_max in range(prime_min, len(primes_below12000)):
        testsum = sum(primes_below12000[prime_min:prime_max])
        if isPrime(testsum) and testsum < 1000000:
            if prime_max - prime_min > maxlength:
                maxlength = prime_max - prime_min
                maxprime = testsum


print(f"The prime, {maxprime} is the sum of {maxlength} consectutive primes.")

