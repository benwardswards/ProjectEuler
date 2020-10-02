"""Integer right triangles

Problem 39

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
from math import sqrt
from typing import Set, FrozenSet


def interger_triangles_perimeter(perimeter: int) -> int:
    setofsolutions: Set[FrozenSet[int]] = set()
    for h in range(1, perimeter // 2 + 1):
        for b in range(1, perimeter // 2 + 1):
            if h > b:
                if perimeter - h - b <= b:  # save computation
                    if perimeter - h - b == sqrt(h ** 2 - b ** 2):
                        setofsolutions.add(frozenset({perimeter - h - b, b, h}))
    # print(perimeter, setofsolutions, len(setofsolutions))
    return len(setofsolutions)


assert interger_triangles_perimeter(120) == 3

pmax = 0
maxvalue = 0
print("p, number of solutions")
for p in range(2, 1001):
    tempmax = interger_triangles_perimeter(p)
    if tempmax > 0:
        print(p, tempmax)
    if tempmax > maxvalue:
        maxvalue = tempmax
        pmax = p

print(f"The perimeter with the most solutions is {pmax} with {maxvalue} solutions")

