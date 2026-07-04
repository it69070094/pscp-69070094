"docstring"
NAME = input()
SURNAME = input()
AGE = input()

if len(NAME) >= 5 and len(SURNAME) >= 5:
    RESURNAME = SURNAME[::-1]
    REAGE = AGE[::-1]
    print(NAME[0]+NAME[1]+RESURNAME[0]+REAGE[0])
elif len(NAME) < 5 or len(SURNAME) < 5:
    RESURNAME = SURNAME[::-1]
    print(NAME[0]+AGE+RESURNAME[0])
