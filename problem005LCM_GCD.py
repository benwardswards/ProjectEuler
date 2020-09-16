# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?
from numba import jit
from functools import reduce

# This is way too slow:
@jit(nopython=True)
def divides_2to20(count):
    found = True
    for i in range(2, 11):
        if count % i != 0:
            # print(count,i)
            break
        if i == 20:
            found = False
    return found


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


assert lcm(5, 2) == 10
assert lcm(2, 5) == 10

assert lcm(12, 4) == 12
assert lcm(15, 6) == 30


print(
    "The smallest number divisilbe by the numbers 2-10 is : ", reduce(lcm, range(2, 11))
)

print(
    "The smallest number divisilbe by the numbers 2-10 is : ", reduce(lcm, range(2, 21))
)
