year = int(input("Enter the year to check if it is leap year or not : "))

if year%4==0 or year%400==0:
    print("Leap year!")
else:
    print("Not a leap year!")