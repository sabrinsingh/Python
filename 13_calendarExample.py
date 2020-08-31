#import calendar module
import calendar

print(calendar.month(2020, 8))


# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2017, 1, 0, 0)
print (str)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2017, 1)
print (str)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2017, 8):
  print (i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
  print (name)

for day in calendar.day_name:
  print (day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print ("Team meetings will be on:")
for m in range(1,13):
  # returns an array of weeks that represent the month
  cal = calendar.monthcalendar(2018, m)
#   print(cal)
  # The first Friday has to be within the first two weeks
  weekone = cal[0]
  weektwo = cal[1]
#   print("hahahahahaahah", calendar.month_name[m], weekone[calendar.FRIDAY])
   
  if weekone[calendar.FRIDAY] != 0:
    meetday = weekone[calendar.FRIDAY]
  else:
    # if the first friday isn't in the first week, it must be in the second
    meetday = weektwo[calendar.FRIDAY]
      
  print ("%s %d" % (calendar.month_name[m], meetday))
