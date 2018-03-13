year = input("enter a year : ")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print "%s is a leap year"%year
        else:
            print "%s is not a leap year"%year
    else:
        print "%s is a leap year"%year
else:
    print "%s is not a leap year"%year
