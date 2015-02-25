##You are given the following information, but you may prefer to do some
##research for yourself.
##
##1 Jan 1900 was a Monday.
##Thirty days has September,
##April, June and November.
##All the rest have thirty-one,
##Saving February alone,
##Which has twenty-eight, rain or shine.
##And on leap years, twenty-nine.
##A leap year occurs on any year evenly divisible by 4, but not on a century
##unless it is divisible by 400.
##How many Sundays fell on the first of the month during the twentieth century
##(1 Jan 1901 to 31 Dec 2000)?
##1 Jan 1901 was a Tuesday
from time import time
t1=time()
md = [31,28,31,30,31,30,31,31,30,31,30,31]
# [1=mon,2=tues,3=wed,4=thur,5=fri,6=sat,7=sun]
day=1 # Start on Monday, Dec 31, 1900
sundays=0
for year in range(1901,2001):
    for month in md:
        if not year%400 and month==28 and year!=2000:
            month=29    
        day+=month
        if day%7==1:
            sundays+=1
print(sundays)
print(time()-t1)
