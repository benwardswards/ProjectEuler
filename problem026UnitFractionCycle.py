"""A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part."""

from typing import List


def decimalunitfraction(n: int) -> int:
    expansionList: List[int] = []
    remainderList: List[int] = []
    remainder = 10
    # counter = 1
    while remainder != 0:
        expansionList.append(remainder // n)
        remainder = (remainder % n) * 10
        remainderList.append(remainder)
        cyclicLength = isThereCycle(expansionList, remainderList)
        if cyclicLength > 0 and len(expansionList) > 2 * cyclicLength:
            return cyclicLength

    print(expansionList)
    return 0


def isThereCycle(expList: List[int], remainList: List[int]) -> int:
    # print("len of expList is", len(expList)//2)
    n = len(expList)
    for i in range(1, len(expList) // 2 + 1):
        if (
            expList[n - 2 * i : n - i] == expList[n - i : n]
            and remainList[n - 2 * i : n - i] == remainList[n - i : n]
        ):
            # print(f"we have a cycle of length: {i}")
            return i
    return 0


print("1/100 is ", decimalunitfraction(100))
print("1/101 is ", decimalunitfraction(101))


for i in range(1, 1):
    print("1/", i, "has a cycle of length ", decimalunitfraction(i))

a = [1, 2, 3, 4, 5, 6]
n = len(a)
for i in range(1, 3 + 1):
    print(a[n - 2 * i : n - i], a[n - i : n])
print("testing isThereCycle")
print(isThereCycle([1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3]))
print(isThereCycle([0, 1, 2, 3, 1, 2, 3], [0, 1, 2, 3, 1, 2, 3]))
print(isThereCycle([0, 3, 4, 5, 1, 2, 3, 1, 2, 3], [0, 3, 4, 5, 1, 2, 3, 1, 2, 3]))
print(isThereCycle([0, 3, 4, 5, 1, 2, 3, 1, 2, 2], [0, 3, 4, 5, 1, 2, 3, 1, 2, 2]))
print(
    isThereCycle([7, 0, 3, 4, 5, 1, 2, 1, 3, 1, 3], [7, 0, 3, 4, 5, 1, 2, 1, 3, 1, 3])
)


assert decimalunitfraction(2) == 0
assert decimalunitfraction(4) == 0
assert decimalunitfraction(9) == 1
assert decimalunitfraction(7) == 6


maxvalue = 0
maxindex = 1
for denom in range(1, 1000):
    tempmaxvalue = decimalunitfraction(denom)
    print("1/", denom, "has a cycle of length ", tempmaxvalue)
    if tempmaxvalue > maxvalue:
        maxindex = denom
        maxvalue = tempmaxvalue

print("maxcycle is for ", maxindex, " with length ", maxvalue)
