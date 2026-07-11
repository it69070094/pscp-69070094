#ถ้าค่าน้อยที่สุดที่เป็นไปได้คือมีmax2ค่าและmin1ค่า
# max + max + min = total ---> 2 * max + min = total
# min = total - (2max)

"docstring"
total = float(input())
highest = float(input())
lowest = total - (highest * 2)

if lowest < 0:   #ไม่ให้มีค่าต่ำกว่า0
    lowest = 0

if highest - lowest > 2:
    print("Surprising")
else:
    print("Not surprising")
