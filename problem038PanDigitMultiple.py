"""Pandigital multiples  Problem 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?"""

from typing import List


def listToNumber(numList: List[int]) -> int:
    s = "".join([str(i) for i in numList])
    return int(s)


assert listToNumber([1, 2, 3, 4]) == 1234


def numberToList(number: int) -> List[int]:
    return [int(digit) for digit in str(number)]


assert numberToList(1234) == [1, 2, 3, 4]


def concatnumbers(listnumbers: List[int]) -> List[int]:
    listofdigits = []
    for num in listnumbers:
        for digit in numberToList(num):
            listofdigits.append(digit)
    return listofdigits


assert concatnumbers([1, 23, 45, 6, 789]) == list(range(1, 10))


def panDigit(start):
    for max_n in range(2, 11):
        listofnums: List[int] = [i * start for i in range(1, max_n)]
        listofdigits: List[int] = concatnumbers(listofnums)
        # print(listofdigits)
        if len(listofdigits) > 9:
            return 0
        if len(listofdigits) == 9:
            if set(listofdigits) == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return listToNumber(listofdigits)

    return 0


assert panDigit(1) == 123456789
assert panDigit(192) == 192384576
assert panDigit(9) == 918273645

maxes = [panDigit(i) for i in range(1, 10000) if panDigit(i) > 0]
print("The Largest pan digit multiple is:", max(maxes))
