"""
@Author: Shubham shirke
@Date: 2021-02-11 18:00:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-02 13:05:30
@Title : To check the given year is leap year or not.
"""

def check_leap_year(year):
   if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
   else:
    print(year, "is not a leap year")


year=int(input("Enter year to check leap year: "))
check_leap_year(year)

