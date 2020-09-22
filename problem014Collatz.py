# runs fast on pypy or with jit compared to cpython

from numba import jit


@jit(nopython=True)
def collatzLength(num: int) -> int:
    length: int = 1
    while num != 1:
        length += 1
        if num % 2:
            num = 3 * num + 1
        else:
            num = num // 2
    return length


assert collatzLength(1) == 1
assert collatzLength(2) == 2
assert collatzLength(13) == 10

longestNumber: int = 1
lengthofLongestNumber: int = 1
for ic in range(1, 1000000):
    ic_length = collatzLength(ic)
    if ic_length > lengthofLongestNumber:
        lengthofLongestNumber = ic_length
        longestNumber = ic

print(
    "The number less than a million with the longest collatz sequence is: ",
    longestNumber,
    " with collatz length",
    ic_length,
)

