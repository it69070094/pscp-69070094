"docstring"
CHAR = input()
NUM = input()

if CHAR == "H" and NUM == "4567":
    print("safe unlocked")
elif CHAR != "H" and NUM == "4567":
    print("safe locked - change char")
elif CHAR == "H" and NUM != "4567":
    print("safe locked - change digit")
elif CHAR != "H" and NUM != "4567":
    print("safe locked")
