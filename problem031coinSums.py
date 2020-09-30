"""Coin sums

Problem 31
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

"""
from itertools import product
from typing import List

coins: List[int] = [1, 2, 5, 10, 20, 50, 100, 200]
maxcoins = [200 // coin + 1 for coin in coins]

TOTAL: int = 200
combination_count: int = 0

all_products = product(
    range(maxcoins[1]),
    range(maxcoins[2]),
    range(maxcoins[3]),
    range(maxcoins[4]),
    range(maxcoins[5]),
    range(maxcoins[6]),
    range(maxcoins[7]),
)


for prod in all_products:
    if (
        sum(number_of_coins * coin for number_of_coins, coin in zip(prod, coins[1:]))
        <= TOTAL
    ):
        combination_count += 1


print(f"The number of valid combinations is {combination_count}")

