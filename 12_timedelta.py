from datetime import date, datetime, time, timedelta

#construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1))

#print today's date
now=datetime.now()
print("Today is " + str(now))

#print 1 years from now
print("1 year from would be " + str(now + timedelta(days=365)))

#using more than one argument
print("In 4 days and 3 weeks, it will be " + str(now + timedelta(days=2, weeks=3)))
print("4 days and 3 weeks ago, it was  " + str(now - timedelta(days=2, weeks=3)))

#how many days until my birthday?
today = date.today()
bday = date(today.year, 5 ,28)

print(bday)
 # if bday is gone, add a year to it (using replace function) and calculate again
if bday < today:
    print("Its gone for this year by %d days "   %((today-bday).days))
    bday=bday.replace(year=today.year+1)
    # print(bday)
    # bday = bday + timedelta(days=365)
    print(bday)

print("For next bday, days remaining is " + str((bday-today).days))
print("For next bday, days remaining is %d"  %((bday-today).days))