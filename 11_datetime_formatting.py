from datetime import date
from datetime import time
from datetime import datetime

#Tmes and dates can be formatted using a set of predefiened string
now = datetime.now()

#%y/%y - Year, %a/%A - weekday, %b/%B -month, %d - day of month
print(now.strftime("The current year is : %Y , weekday is %a , month is %b and the day of month is %d"))

# %c - locale's date and time,  %x - locale's date, %X - locales's time
print(now)
print(now.strftime("Locale date and time : %c"))
print(now.strftime("Locale date : %x"))
print(now.strftime("Locale time : %X"))


#### TIME FORMATTNG ####

# %I/%H - 12/24 hour, %m - minute, %S - second, %p - Locale's AM/PM
print(now.strftime("Current time : %I:%m:%S:%p"))
print(now.strftime("24 hr - Current time : %H:%m:%S:%p"))