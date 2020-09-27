"""Quadratic primes
  Show HTML problem content  
Problem 27
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n**2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

from utils import isPrime

from itertools import product


def numberofPrimesQuadratic(a: int, b: int) -> int:
    n: int = 0
    while isPrime(n ** 2 + n * a + b):
        n += 1
    return n


assert numberofPrimesQuadratic(1, 41) == 40
assert numberofPrimesQuadratic(-79, 1601) == 80

maxvalue: int = -1
maxa: int = 0
maxb: int = 0
for a, b in product(range(-1000 + 1, 1000), range(-1000 + 1, 1000)):
    tempmax = numberofPrimesQuadratic(a, b)
    if tempmax > maxvalue:
        maxvalue = tempmax
        maxa = a
        maxb = b

print(
    f" max number of consecutive primes is {maxvalue}, where a={maxa}, b={maxb}, a*b={maxa * maxb}"
)
# print(numberofPrimesQuadratic(99, 100))
