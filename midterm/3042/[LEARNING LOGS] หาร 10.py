"หาร10ลงตัว"
n = int(input())

box = []
i = 0
z = 0
y = int(n / 10)
for i in range(y):
    i += 1
    z += 10
    box.append(z)
    box.sort()
    box = box[::-1]
print(*box , 0)
