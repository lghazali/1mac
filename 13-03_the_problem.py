# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    if year % 4 != 0: return False
    if year % 100 != 0: return True
    if year % 400 != 0: return False
    return True

    # Proc to check that inputs are VALID dates
def checkValidDate(y, m, d):
    if m < 1 or m > 12: return False
    if d < 1: return False
    if isLeapYear(y) and m == 2 and d != 29: return False
    if d > daysOfMonths[m-1]: return False
    return True

    # Proc to Check if date 1 is before date 2
def checkDateIsBefore(y1,m1,d1,y2,m2,d2):
    if y1 > y2: return False
    if y1 == y2 and m1 > m2: return False
    if m1 == m2 and d1 > d2: return False
    return True

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    # Check that inputs are VALID dates
    if not checkValidDate(y1,m1,d1) or not checkValidDate(y2,m2,d2):
        print "Invalid dates were given"
        return -1

    #   Check that 21st date is BEFORE 2nd date
    if not checkDateIsBefore(y1,m1,d1,y2,m2,d2):
        # if date 1 is after date 2 "Time Travel", swap the dates
        print "Date 1 is after date 2, I swapped the dates for you"
        y3 = y1; m3 = m1; d3 = d1
        y1 = y2; m1 = m2; d1 = d2
        y2 = y3; m2 = m3; d2 = d3

    ## Calculate days ##
    # Set days initially to 0
    days = 0
    # Keep adding days of each month until we reach 1 year before end year
    while y1 < y2:
        # If February, then check for leap year
        if m1 == 2:
            if isLeapYear(y1): days += 29
            else: days += 28
        # Else add days of relevant month
        else:
            days += int(daysOfMonths[m1-1])
        # Keep going by adding 1 month
        # and set m1 to 1 after 12 and add 1 year to y1
        if m1 < 12:
            m1 += 1
        else:
            m1 = 1
            y1 += 1
    # When we reach end year, we add daysOfMonths
    # until 1 month before end month
    while m1 < m2 and m1<= 12:
        if m1 == 2:
            if isLeapYear(y1): days += 29
            else: days += 28
        else:
            days += int(daysOfMonths[m1-1])
        m1 += 1
    # When we reach end month we add 1 day at a time
    # until 1 day before target day
    while d1 < d2:
        days += 1
        d1 += 1
    # We're done
    return days

## Test the program ##
age_days = daysBetweenDates(2012, 12, 8, 2012, 12, 7)
if age_days >= 0:
    print "Your age in days is: " + str(age_days)

#yearl = 2016
#print str(yearl) + " " + str(isLeapYear(yearl))
