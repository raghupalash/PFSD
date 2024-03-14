year = int(input("Year: "))

r = year % 4

if r == 0:
    print("It's a leap year!")
else:
    print("It's not a leap year!")
