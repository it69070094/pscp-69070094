"หมึกกระจากตัวไปโดนบ้านตอนไหน"
import math as m
S , N = map(int, input().split())
box = []
i = 0
for i in range(N):
    i += 1
    x , y = map(int, input().split())
    r = x**2 + y**2
    time = (3.1416 * r) / S
    box.append(time)

for num in box:
    print(m.ceil(num))
