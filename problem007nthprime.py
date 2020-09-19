# Find the 10001 prime number
from math import sqrt


def isPrime(number):
    if number in (0, 1):
        return False

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def yieldPrime():
    count = 1
    while True:
        if isPrime(count):
            yield count
        count += 1


primes = yieldPrime()
assert next(primes) == 2
assert next(primes) == 3
assert next(primes) == 5


def nthPrime(howmany):
    primes = yieldPrime()
    for _ in range(howmany):
        prime = next(primes)
    return prime


print("The 6th prime is ", nthPrime(6))
print("The 10001 prime is ", nthPrime(10001))
