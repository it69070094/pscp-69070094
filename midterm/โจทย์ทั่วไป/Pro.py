"docsting"
X = int(input())
Y = int(input())
A = int(input())
Z = int(input())

SETS = Z // X
REMAIN = Z % X

TOTAL = SETS * (Y * A) + (REMAIN * A)

print(TOTAL)
