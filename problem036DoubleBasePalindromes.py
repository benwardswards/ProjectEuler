"""	
Double-base palindromes
Problem 36

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)"""
from typing import List


def numberToList(number: int) -> List[str]:
    return [digit for digit in str(number)]


def numberToListBase2(number: str) -> List[str]:
    return [digit for digit in str(number)[2:]]


def isDoublePalindrome(number: int) -> bool:
    listofdigits: List[str] = numberToList(number)
    if listofdigits == listofdigits[::-1]:
        isPalindrome10 = True
    else:
        isPalindrome10 = False

    numberbase2 = bin(number)
    # print(type(numberbase2))
    listofdigitsb2: List[str] = numberToListBase2(numberbase2)
    if listofdigitsb2 == listofdigitsb2[::-1]:
        isPalindromeB2 = True
    else:
        isPalindromeB2 = False

    return isPalindrome10 and isPalindromeB2


# a = bin(121)
# print(a, str(a)[2:-1])

assert isDoublePalindrome(3) == True
assert isDoublePalindrome(585) == True
assert isDoublePalindrome(121) == False
assert isDoublePalindrome(3443) == False
assert isDoublePalindrome(1223) == False

doublePalindromes = [i for i in range(1, 1_000_001) if isDoublePalindrome(i)]

print("Double palindromes:")
for palin in doublePalindromes:
    print(palin, bin(palin))
print(f"The sume of the Double palindroms below 1 million is {sum(doublePalindromes)}")
