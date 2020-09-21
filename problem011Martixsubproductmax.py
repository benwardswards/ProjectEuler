import numpy as np
from typing import List

y = np.loadtxt("problem011.txt", delimiter=" ", dtype=int)

print(y)
nr, nc = np.shape(y)
assert (nr, nc) == (20, 20)

prodLength: int = 4
maximums: List[int] = []


def maxUpdown(matrix, length: int = 4) -> int:
    """Find the maximum product of four numbers next to each other in a column 
    """
    nr, nc = np.shape(matrix)
    maxproduct1: int = 0
    for icol in range(nc):
        for irow in range(nr - prodLength):
            runningsum = np.prod(matrix[irow : irow + prodLength, icol])
            if runningsum > maxproduct1:
                maxproduct1 = runningsum

    return maxproduct1


maximums.append(maxUpdown(y))


def maxLeftright(maxtrix, length: int = 4) -> int:
    return maxUpdown(np.transpose(maxtrix), prodLength)


maximums.append(maxLeftright(y))


def maxDiagnol(matrix, prodLength: int = 4):
    nr, nc = np.shape(matrix)
    maxproduct1 = 0
    for icol in range(nc - prodLength):
        for irow in range(nr - prodLength):
            runningsum = (
                matrix[irow, icol]
                * matrix[irow + 1, icol + 1]
                * matrix[irow + 2, icol + 2]
                * matrix[irow + 3, icol + 3]
            )
            if runningsum > maxproduct1:
                maxproduct1 = runningsum
    return maxproduct1


maximums.append(maxDiagnol(y))

maximums.append(maxDiagnol(y[::-1, :]))

print(maximums)
print("The max product is ", max(maximums))
