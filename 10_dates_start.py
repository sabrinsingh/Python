from datetime import date
from datetime import time
from datetime import datetime

#print out todays date
today=date.today()
print(today)

#print out the date's individual components
print("Date components: " , today.day, today.month, today.year)

#print out the week day number
#In python date starts from MONDAY. So if its Monday, then weekday is 0.
print("Today's weekday is ", today.weekday())

#Get today's date from the datetime class
print(datetime.now())

#Get the current time only
print(datetime.time(datetime.now()))



# calendar program that needs to print tomorrow's day of the week.
today=date.today()
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
print("Tomorrow will be "+days[(today.weekday()+1)%7])