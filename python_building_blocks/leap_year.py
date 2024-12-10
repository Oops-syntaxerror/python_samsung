# Check the given user year is a Leap Year.
 
year = int(input('Enter any year:'))
 
if ( year % 4 == 0 & year % 100 == 0 ) | ( year % 4 == 0 & year % 100 != 0):
    print(year,'is a Leap Year.') 