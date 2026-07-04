"docstring"
RA = int(input())
RB = int(input())
STRING = input()

EA = 1/(1+(10**((RB-RA)/400)))
EB = 1/(1+(10**((RA-RB)/400)))

if STRING == "A":
    print(f"{EA:.2f}")
elif STRING == "B":
    print(f"{EB:.2f}")
