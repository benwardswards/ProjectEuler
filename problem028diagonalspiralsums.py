"""Number spiral diagonals
  Show HTML problem content  
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""


def diagonalSpiralSums(n: int) -> int:
    index: int = (n - 1) // 2  # length of the diagnol from the center
    sum_four_corners = lambda i: 4 * (2 * i + 1) ** 2 - 12 * i
    ## 4 * upper corner 1, 9, 25 - offset of the 3 other corners
    return 1 + sum([sum_four_corners(i) for i in range(1, index + 1)])


for n in [1, 3, 5, 7, 1001]:
    print(f"A spiral of size {n} has a sum of diagonls of {diagonalSpiralSums(n)}")


# for index in range(1, 14, 2):
#    print(diagonalSpiralSums(index) - diagonalSpiralSums(index - 1))
