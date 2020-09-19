"""The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""


def sumofsquare(N: int) -> int:
    return sum(i * i for i in range(N + 1))


assert sumofsquare(4) == 1 + 4 + 9 + 16


def thesquareofthesum(N: int) -> int:
    return sum(i for i in range(N + 1)) ** 2


assert thesquareofthesum(4) == 100

assert thesquareofthesum(10) - sumofsquare(10) == 3025 - 385


print("The Square of the sum minus the sum of squares of the first 100 numbers is: ")

print(thesquareofthesum(100) - sumofsquare(100))

