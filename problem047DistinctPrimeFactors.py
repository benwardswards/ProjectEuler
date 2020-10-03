"""Distinct primes factors
Problem 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

from typing import List, Set
from utils import isPrime


def number_of_prime_factors(n: int) -> int:
    i: int = 2
    factors: Set[int] = set()
    while i * i <= n:  # cheaper than i < sqrt(n)
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    # print(factors)
    return len(set(factors))


assert number_of_prime_factors(14) == 2
assert number_of_prime_factors(15) == 2
assert number_of_prime_factors(644) == 3
assert number_of_prime_factors(645) == 3
assert number_of_prime_factors(646) == 3
assert number_of_prime_factors(9) == 1
assert number_of_prime_factors(120) == 3
assert number_of_prime_factors(2 * 3 * 5 * 7) == 4
assert number_of_prime_factors(2 * 3 * 5 * 7 * 7) == 4


def first_n_consecutive_n_prime_factors(n: int) -> List[int]:
    num: int = 2
    while not all(number_of_prime_factors(i) == n for i in range(num, num + n)):
        num += 1
    return [i for i in range(num, num + n)]


assert first_n_consecutive_n_prime_factors(2) == [14, 15]

print("The first 3 consecutive numbers with 3 distinct prime factors ")
print(first_n_consecutive_n_prime_factors(3))

print("The first 4 consecutive numbers with 4 distinct prime factors ")
print(first_n_consecutive_n_prime_factors(4))

