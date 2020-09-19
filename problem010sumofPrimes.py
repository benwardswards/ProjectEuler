# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from math import sqrt
from utils import isPrime, nextprime


def sum_of_primes(maxprime: int) -> int:
    """Returns the sum of all the primes strictly less than maxprime.
    """
    primes = nextprime()
    prime = next(primes)
    sumofprimes: int = 0
    while prime < maxprime:
        sumofprimes += prime
        prime = next(primes)

    return sumofprimes


assert sum_of_primes(5) == 2 + 3
assert sum_of_primes(10) == 2 + 3 + 5 + 7

print(f"The sum of primes below 2_000_000 is : {sum_of_primes(2_000_000)}")

