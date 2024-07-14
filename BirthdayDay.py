#!/usr/bin/python3
from datetime import date
"""
Python version of the program
@author Jonathan Hsin
@date 7/14/2024
"""

"""
checks if a year is a leap year
"""
def isLeap(year:int)->bool:
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#testing the leap year checker
assert isLeap(2024)==True
assert isLeap(2023)==False
assert isLeap(1900)==False
assert isLeap(2000)==True
"""
checks that a date is valid
returns true if date is valid and false otherwise
"""
def valiDATE(month:int, day:int, year:int)->bool:
    dates_of_months=[31,28,31,30,31,30,31,31,30,31,30,31]
    #change the number of days in February if it is a leap year
    if isLeap(year):
        dates_of_months[1]=29
    return month>0 and month<=12 and day>0 and day<=dates_of_months[month-1] and year>0
#testing the valiDATE method
assert valiDATE(2,29,2024)==True
assert valiDATE(2,29, 2023)==False
assert valiDATE(2,29,1900)==False
assert valiDATE(2,29,2000)==True
assert valiDATE(1,31,2023)==True
assert valiDATE(4,30,2023)==True
assert valiDATE(4,31,2023)==False
assert valiDATE(13,1,2023)==False
assert valiDATE(1,0,2023)==False
assert valiDATE(2,28,2024)==True
assert valiDATE(2,28,2024)==True

"""
using Zeller's congruence, calculate the day of the week given the date
returns:
0=Saturday
1=Sunday
2=Monday
3=Tuesday
4=Wednesday
5=Thursday
6=Friday
"""
def zeller(month:int, day:int, year:int)->int:
    #first adjust if the month is January or February
    if month==1:
        month=13
        year-=1
    elif month==2:
        month=14
        year-=1
    j=year//100
    k=year%100
    return (day+(13*(month+1)//5)+k+(k//4)+(j//4)-(2*j))%7
#testing the zeller function
assert zeller(7,14,2024)==1
assert zeller(1,6,2024)==0

#first prompt for the user's birthday
valid=False
#loops the program until a valid date is given
while not valid:
    bdaystr=input("Please enter your birthday in mm/dd/yyyy form(ex:1/1/2000):\n")
    #check that the date is "/" delimited
    valid="/" in bdaystr
    if valid:
        #split the string using delimeter
        bday=bdaystr.split("/")
        #check that the string can be converted to integer
        valid=(len(bday)==3) and (not bday[0]=="" and bday[0].isdigit()) and (not bday[1]=="" and bday[1].isdigit()) and (not bday[2]=="" and bday[2].isdigit())
        if valid:
            month=int(bday[0])
            day=int(bday[1])
            year=int(bday[2])
            #validate date based on the numbers
            valid=valiDATE(month, day, year)
    if not valid:
        print("That is not a valid date")

#once a valid birthday is inputted, first check what day of the week this year will be
#first define a list of the days of the week based on the output from Zeller's Congruence
weekdays=["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
today=str(date.today()).split("-")
curryear=int(today[0])
print("This year("+str(curryear)+"), your birthday is on a "+weekdays[zeller(month, day, curryear)]+"\n\n")

#now ask the user what years they want to look at until they quit
quit=False
while not quit:
    curryear=input("What other years do you want to know what day your birthday will be on?(enter year or q to quit)\n")
    if curryear=="q":
        quit=True
    elif not curryear.isdigit():
        print("\""+curryear+"\" is not a valid year, please try again")
    else:
        print("In "+curryear+", your birthday is on a "+weekdays[zeller(month, day,int(curryear))]+"\n")