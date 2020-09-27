"""The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
from typing import Iterator


def fibonacci() -> Iterator[int]:
    a: int = 1
    b: int = 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


fib1 = fibonacci()
print([next(fib1) for _ in range(12)])

# setting up while loop
fib_itr = fibonacci()
count: int = 1
next_fib: int = next(fib_itr)
TEN_TO_999: int = 10 ** 999
while next_fib <= TEN_TO_999:
    count += 1
    next_fib = next(fib_itr)


print(next_fib, " is fist number bigger the 10**999 at index ", count)

