"""Calendar Maker, by Al Sweigart al@inventwithpython.com
Create monthly calendars, saved to a text file and fit for printing.
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: short"""

import datetime

# set up the constants:
DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 
          'September', 'October', 'Novermeber', 'December')

print('Calendar Maker, by James Matyka')

while True: # Loop to get a year from the year
    print('Enter the year for the calendar:')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year, like 2023')
    continue

while True: # Loop to get a month from the user.
    print('Enter the month for the calendar, 1-12:')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March.')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number from 1 to 12')

def getCalendarFor(year, month):
    calText = ''  # calText will contain the string of our calendar.

    # Put the month and year at the top of the calendar:
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'

    # Add the days of the week labels to the calendar:
    # (!) Try changing this to abbreviations: SUN, MON, TUE, etc.
    calText += '...Sunday....Monday....Tuesday....Wednesday....Thurdsay....Friday....Saturday'

    # The horizontal line string that separate weeks:
    weekSeparator = ('+----------' * 7) + '+\n'

    # The blank rows have ten spaces in between the | day separators:
    blankRow = ('|          ' * 7) + '|\n'

    # Get the first date in the month. ( The dateime module handles all 
    # the complicated calendar stuff or us here.
    currentDate = datetime.date(year, month, 1)

    # Roll back currentDate until it is Sunday (weekday() returns 6 for sunday, not 0)
    while currentDate.weekday()!= 0:
        currentDate -= datetime.timedelta(days=1)
    
    while True: # Loop over each week in the month.
        calText += weekSeparator

        # dayNumberRow is the row with the day number labels:
        daysNumberRow = ''
        for i in range(7):
            daysNumberLabel = str(currentDate.day).rjust(2)
            daysNumberRow += '|' + daysNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1) # Go to the next day
        daysNumberRow += '|\n' # Add the vertical line after Saturday

        # Add the day number row and 3 blank rows to the calendar text.
        calText += daysNumberRow
        for i in range(3):  # (!) try changing this
            calText += blankRow

        # Check if we're done with the month:
        if currentDate.month != month:
            break

    #  Add the horizontal line at the very bottom of the calendar.
    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print(calText) # Display the calendar

# Save the calendar to a text file:
calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)