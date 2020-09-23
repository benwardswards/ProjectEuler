"""You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from typing import Dict

def days_of_the_year(year: int) -> int: 
    days_in_year: int = 30*4+31*7+28
    if year % 4 == 0:
        days_in_year += 1
    if year % 100 ==0:
        days_in_year += -1
    if year % 400 ==0:
        days_in_year += 1

    return days_in_year

#print(days_of_the_year(1900))

assert days_of_the_year(1980) == 366
assert days_of_the_year(1901) == 365
assert days_of_the_year(400) == 366
assert days_of_the_year(100) == 365

days_in_a_week: int = 7

def days_in_a_month(year:int , month: int ) -> int:
    days_in_feb: int = 28
    if year % 4 == 0:
        days_in_feb += 1
    if year % 100 ==0:
        days_in_feb += -1
    if year % 400 ==0:
        days_in_feb += 1

    monthsdict: Dict[int, int] = {1:31, 2:days_in_feb, 3:31, 4:30, 5: 31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31,}

    #print(sum(monthsdict.values()))
    return monthsdict[month]

assert days_in_a_month(1900,3) == 31
assert days_in_a_month(1980,2) == 29
assert days_in_a_month(1981,2) == 28

"""
def mtwtfss() -> Iterator:
    firstdayof1900 = 0
    while True:
        firstdayof1900 = (firstdayof1900+1)%7
        yield firstdayof1900



def number_mondays_on_a_first(yearstart: int, yearend: int) -> int:
    firstmonday = 1900
    return firstmonday
"""

dayofweek: int = 1
numberOfMbBeginWithS: int = 0

year: int= 1900
for month in range(1,13):
    dayofweek = (dayofweek + days_in_a_month(year,month)) % 7
    print(year,month,dayofweek)

print("fist day of 1901 is a ", dayofweek )
for year in range(1901,2001):
    for month in range(1,13):
        if dayofweek == 0:
            numberOfMbBeginWithS += 1
        dayofweek = (dayofweek + days_in_a_month(year,month)) % 7

print("number of months that begin with sundays is ", numberOfMbBeginWithS)

assert sum([days_in_a_month(1980, month)  for month in range(1,13)]) == 366