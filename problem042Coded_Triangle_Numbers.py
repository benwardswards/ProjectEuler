"""Coded triangle numbers
  Show HTML problem content  
Problem 42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
import string
import csv
from typing import List, Dict
from random import choice

triangle_numbers: List[int] = [n * (n + 1) // 2 for n in range(1, 30)]

assert triangle_numbers[3] == 10
assert triangle_numbers[4] == 15

lettervalue: Dict[str, int] = dict(zip(string.ascii_lowercase, range(1, 27)))

assert lettervalue["a"] == 1
assert lettervalue["z"] == 26


def word_value(word: str) -> int:
    return sum(lettervalue[letter] for letter in word.lower())


assert word_value("SKY") == 55
assert word_value("A") == 1
assert word_value("a") == 1

with open("problem042.txt", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:  # there is only one row...
        rawdata: List[str] = row


print("Word, Letter score, Total")
for _ in range(10):
    word: str = choice(rawdata)
    letter_values: List[int] = [lettervalue[letter] for letter in word.lower()]
    print(
        word, letter_values, sum(letter_values),
    )


list_word_values: List[int] = [word_value(nextword) for nextword in rawdata]


assert max(list_word_values) < max(triangle_numbers)

truths: int = sum(1 for score in list_word_values if score in triangle_numbers)

print(f"The number of words with word value that is trianglur is {truths}")
