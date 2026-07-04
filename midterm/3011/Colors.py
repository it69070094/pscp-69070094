"docstring"
COLORA = input()
COLORB = input()

if COLORA == "Red":
    if COLORB == "Yellow":
        print("Orange")
    elif COLORB == "Blue":
        print("Violet")
    elif COLORB == "Red":
        print("Red")
    elif COLORB != "Red" or COLORB != "Yellow" or COLORB != "Blue":
        print("Error")
elif COLORA == "Yellow":
    if COLORB == "Red":
        print("Orange")
    elif COLORB == "Blue":
        print("Green")
    elif COLORB == "Yellow":
        print("Yellow")
    elif COLORB != "Red" or COLORB != "Yellow" or COLORB != "Blue":
        print("Error")
elif COLORA == "Blue":
    if COLORB == "Red":
        print("Violet")
    elif COLORB == "Yellow":
        print("Green")
    elif COLORB == "Blue":
        print("Blue")
    elif COLORB != "Red" or COLORB != "Yellow" or COLORB != "Blue":
        print("Error")
elif COLORA != "Red" or COLORA != "Yellow" or COLORA != "Blue":
    print("Error")
