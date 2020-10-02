"""Pandigital prime

Problem 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import combinations
from itertools import permutations
from functools import reduce
from math import sqrt
from utils import isPrime


assert isPrime(3) == True
assert isPrime(10) == False


listofdigits = "987654321"
numberofdigits = 9
found_a_prime = False

# for i in list(permutations(listofdigits, numberofdigits)):
#   num = int(reduce(lambda a, b : a+b, i))
#    if isPrime(num):
#        print(num, "is prime and pandigit")
#        found_a_prime = True
#        break

print("ok")
num = 10
while not isPrime(
    num
):  # Decreases the number of digits to be found then gernerates the numbers.
    for i in permutations(listofdigits, numberofdigits):
        num = int(reduce(lambda a, b: a + b, i))  # adding strings to make digit
        # print(num)
        if isPrime(num):
            print(num, "is prime and pandigit")
            found_a_prime = True
            break

    # Remove the largest number from the list then keeping looking
    listofdigits = listofdigits[1:]
    numberofdigits -= 1
print(num)
