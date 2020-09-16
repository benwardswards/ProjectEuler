# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from functools import reduce
from typing import List
import math


def isPrime(number: int) -> bool:
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


assert isPrime(2)
assert isPrime(3)
assert isPrime(11)
assert isPrime(10) == False
assert isPrime(12) == False


def largestprimefactor(number: int) -> int:
    num = number
    listofprimefactors = [1]
    maxnum = num // 2 + 1
    i_divisor = 2
    while True:
        if i_divisor >= maxnum:
            listofprimefactors.append(number)
            break
        if number % i_divisor == 0:
            # if isPrime(i_divisor):
            listofprimefactors.append(i_divisor)
            number = number // i_divisor
            maxnum = maxnum // i_divisor + 1
            # print(i_divisor, "number is ", number, "maxnum is ", maxnum)
        else:
            i_divisor = i_divisor + 1

    listofprimefactors.remove(1)
    if listofprimefactors == [1]:
        listofprimefactors.append(num)

    product = reduce((lambda x, y: x * y), listofprimefactors)
    maxp = max(listofprimefactors)
    print(
        num,
        " has prime factors",
        listofprimefactors,
        "which has product",
        product,
        "The largest prime factor is : ",
        maxp,
    )
    return maxp

    # print("The largest prime factor of ", num, " is ", max(listofprimefactors))


largestprimefactor(193)
largestprimefactor(11 * 3 * 2 * 31)
largestprimefactor(144)
largestprimefactor(22)
largestprimefactor(600851475143)

