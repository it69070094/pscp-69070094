"docstring"
temp = float(input())
unit1 = input().upper()
unit2 = input().upper()

def main():
    "docstring"
    if unit1 == "C":
        celsius = temp
    elif unit1 == "K":
        celsius = temp - 273.15
    elif unit1 == "F":
        celsius = (temp - 32) / 1.8
    elif unit1 == "R":
        celsius = (temp / 1.8) - 273.15
    else:
        celsius = temp
    return celsius
main()
def sec():
    "docstring"
    celsius = main()
    retemp = 0
    if unit2 == "C":
        retemp = celsius
    elif unit2 == "F":
        retemp = (celsius * 1.8) + 32
    elif unit2 == "K":
        retemp = celsius + 273.15
    elif unit2 == "R":
        retemp = (celsius + 273.15) * 1.8
    else:
        celsius = temp
    print(f"{retemp:.2f}")
sec()
