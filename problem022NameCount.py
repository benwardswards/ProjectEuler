"""
Names scores

Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import csv
from string import ascii_uppercase
from typing import List

print("Letter Scores:")
for letter in ascii_uppercase:
    print(letter, ord(letter) - ord("A") + 1)


def nameScore(name: str) -> int:
    return sum(ord(letter) - ord("A") + 1 for letter in name)


assert nameScore("COLIN") == 3 + 15 + 12 + 9 + 14

with open("problem022.txt", "rt") as f:
    readCSV = csv.reader(f, delimiter=",")
    names = list(readCSV)

# print(names[0])

names2: List[str] = names[0]
print(type(names2))
print(type(names2[0]))


print(f"Before sorting the first name is : ", names[0][0])

names2.sort()
print("after sorting first name is:", names2[0])
g

score: int = 0
for iname, name in enumerate(names2):
    if iname < 10:
        print(
            f" {name}, {iname + 1}*{nameScore(name)} = {(iname + 1) * nameScore(name)}"
        )
    score += (iname + 1) * nameScore(name)

print(f"The sum of all the name scores is {score}")

