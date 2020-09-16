from math import sqrt


def isPrime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def nextprime():
    number = 2
    while True:
        if isPrime(number):
            yield number
        number += 1


def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        # print(a, b, a % b)
        a, b = b, a % b

    # print(a)
    return a


def lcm(a: int, b: int) -> int:
    """Compute the lowest common multiple of a and b"""
    return a * b // gcd(a, b)
