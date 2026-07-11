"docstring"
month = int(input())
day = int(input())


if 1 <= month <= 3:
    if 1 <= month <= 2:
        print("winter")
    elif month == 3:
        if day < 21:
            print("winter")
        elif day >= 21:
            print("spring")
elif 4 <= month <= 6:
    if 4 <= month <= 5:
        print("spring")
    elif month == 6:
        if day < 21:
            print("spring")
        elif day >= 21:
            print("summer")
elif 7 <= month <= 9:
    if 7 <= month <= 8:
        print("summer")
    elif month == 9:
        if day < 21:
            print("summer")
        elif day >= 21:
            print("fall")
elif 10 <= month <= 12:
    if 10 <= month <= 11:
        print("fall")
    elif month == 12:
        if day < 21:
            print("fall")
        elif day >= 21:
            print("winter")
