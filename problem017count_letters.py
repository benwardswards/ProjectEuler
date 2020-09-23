"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then 
there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""


from typing import Iterator, Dict, List


def numberofletters(number: int) -> int:
    count: int = 0
    letters: Dict = {
        0: 0,
        1: 3,
        2: 3,
        3: 5,
        4: 4,
        5: 4,
        6: 3,
        7: 5,
        8: 5,
        9: 4,
        10: 3,
        11: 6,
        12: 6,
        13: 8,
        14: 8,
        15: 7,
        16: 7,
        17: 9,
        18: 8,
        19: 8,
        20: 6,
    }

    letters_second: Dict = {
        2: 6,
        3: 6,
        4: 5,
        5: 5,
        6: 5,
        7: 7,
        8: 6,
        9: 6,
    }

    if number == 1000:
        # one thousand
        return 11
    twodigitnumber: int = number % 100
    thirddigit: int = number // 100
    if thirddigit != 0:
        # do we need a "hundred"
        count += letters[thirddigit] + 7
        if twodigitnumber != 0:
            # if we need an "and"
            count += 3

    if twodigitnumber < 21:
        count += letters[twodigitnumber]
    elif twodigitnumber < 100:
        first_digit: int = twodigitnumber % 10
        count += letters[first_digit]
        second_digit: int = twodigitnumber // 10
        count += letters_second[second_digit]

    return count


lettercountlist: List[int] = []
for i in range(1, 1001):
    lettercountlist.append(numberofletters(i))

print(lettercountlist)
print(f"The sum of the letter count for the first 1000 numbers {sum(lettercountlist)}")

assert numberofletters(5) == 4
assert numberofletters(21) == 9
assert numberofletters(1000) == 11
assert numberofletters(342) == 23
assert numberofletters(115) == 20
assert numberofletters(900) == 4 + 7
assert numberofletters(901) == 4 + 7 + 3 + 3
assert numberofletters(100) == 3 + 7

