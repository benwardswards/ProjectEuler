"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
 For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
 which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n '
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can 
be written as the sum of two abundant numbers. However, this upper limit cannot be 
reduced any further by analysis even though it is known that the greatest number 
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
import numpy as np
from itertools import product
from math import sqrt
from utils import isPrime


def isAbundant(number: int) -> int:
    listFactors = {1}
    for i in range(2, int(sqrt(number) + 1)):
        if number % i == 0:
            listFactors.add(i)
            listFactors.add(number // i)

    # print(listFactors)
    if number == sum(listFactors):
        print(number, " is perfect")
        return 0
    elif number < sum(listFactors):
        print(number, " is abundant")
        return 1
    else:
        print(number, " is deficent")
        return -1


isAbundant(1)
isAbundant(6)
isAbundant(5)
isAbundant(12)
isAbundant(28)
isAbundant(100)

maxNotAbundant = 28123 + 1
# maxNotAbundant = 100
listofabundant = []
for i in range(1, maxNotAbundant):
    if isAbundant(i) == 1:
        listofabundant.append(i)

print(listofabundant)

setofsumoftwoabundants = set([])
"""
for number in range(1,maxNotAbundant):
    for abun in listofabundant:
        if (number - abun) in listofabundant:
            setofsumoftwoabundants.add(number)
            #print(number, abun, number-abun, isAbundant(abun), isAbundant(number-abun))


"""
for i, j in product(listofabundant, listofabundant):
    if i + j <= maxNotAbundant:
        setofsumoftwoabundants.add(i + j)

# print(setofsumoftwoabundants)
print(f"{len(setofsumoftwoabundants)}")

notsumoftwoabundants = set([])
for i in range(1, maxNotAbundant):
    if i not in setofsumoftwoabundants:
        notsumoftwoabundants.add(i)

print(len(notsumoftwoabundants))

print(
    "the sum of all the positive integers which cannot be written as the sum of two abundant numbers",
    sum(notsumoftwoabundants),
)
