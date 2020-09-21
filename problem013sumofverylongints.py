import numpy as np
import sys

"""Work out the first ten digits of the sum of the following one-hundred 50-digit numbers contained in problem013.txt"""

y = np.loadtxt("problem013.txt", delimiter=" ", dtype=str)
" y is a list of strings"


print(y)
print(f"size of a line converted to an int, {sys.getsizeof(int(y[0]))} Bytes.")
print(
    f"size of the int with just the first 10 digits, {sys.getsizeof(int(y[0][-10:]))} Bytes."
)


sumoflongnumbers: int = 0
for line in y:
    sumoflongnumbers += int(line)


print(
    f"The sum of the numbers is {sumoflongnumbers} which uses {sys.getsizeof(sumoflongnumbers)} bytes of memory, compare to {sys.getsizeof(1000)} bytes for a standard int "
)

tendigits = int(str(sumoflongnumbers)[-10:])

print(f"The first 10 digits are {tendigits}")


""" Lets do it again without using python 3's dynamic ints. Numpy uses fixed precision 32-bit or 64-bit ints. You get overflow using 32 bits """

short_sum = np.array([0], dtype="int64")
print("size of array", sys.getsizeof(short_sum), " bytes")

for line in y:
    short_sum[0] += int(line[-10:])

short_sum[0] = short_sum[0] % 10_000_000_000

print(f"Using fixed precsion numpy arrays the first 10 digits is {short_sum[0]}")

