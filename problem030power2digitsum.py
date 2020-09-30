"""Digit fifth powers
  Show HTML problem content  
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1**4 + 6**4 + 3**4 + 4**4
8208 = 8**4 + 2**4 + 0**4 + 8**4
9474 = 9**4 + 4**4 + 7**4 + 4**4
As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
from typing import List


def prod_digits(power: int, number: int) -> int:
    return sum([int(digit) ** power for digit in str(number)])


assert prod_digits(4, 1634) == 1634


def sum_of_prod_digits(power: int) -> int:
    for n in range(3, 13):
        if 10 ** n - n * 9 ** power > 0:
            max_int: int = 10 ** n
            break
    print("max possible power :", max_int)

    list_of_power: List[int] = []
    for num in range(2, max_int):
        if num == prod_digits(power, num):
            list_of_power.append(num)

    print(f"The list of {power}-powers is : {list_of_power}")
    print(f"The sum of the list of {power}-th digit powers is : {sum(list_of_power)}")

    return sum(list_of_power)


assert sum_of_prod_digits(4) == 19316

sum_of_prod_digits(5)
