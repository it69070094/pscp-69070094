"how many walls to break"
import math as m

n = int(input())
floor = m.ceil(m.sqrt(n))
wall = 0
if not floor % 2:
    if not n % 2:
        wall = (floor - 1) * 2
    if n % 2 == 1:
        wall = ((floor - 1) * 2) - 1
elif floor % 2 == 1:
    if n % 2 == 1:
        wall = (floor - 1) * 2
    if not n % 2:
        wall = ((floor - 1) * 2) - 1
print(wall)
