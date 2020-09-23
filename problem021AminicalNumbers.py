"""Amicable numbers

Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from typing import List
from typing import Set


def properDivisorsSum(number: int) -> int:
    listOfProperDivisors: List[int] = [1]

    listOfProperDivisors = [i for i in range(1, number) if number % i == 0]
    return sum(listOfProperDivisors)


# print(properDivisorsSum(7))
# print(properDivisorsSum(220))

Amicables: Set[int] = set()
for i in range(1, 10000):
    maybeAmicable = properDivisorsSum(i)
    if i == properDivisorsSum(maybeAmicable) and maybeAmicable != i:
        Amicables.add(i)
        print(i, maybeAmicable)

print(Amicables, "The sum of amimibles<10000 is ", sum(Amicables))
