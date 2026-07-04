"docstring"
BILL =  int(input())

SERVICE = ( 10 / 100 ) * BILL
if SERVICE < 50:
    SERVICE = 50
    VAT = ( 50 + BILL ) * ( 7 / 100 )
    print(f"{BILL+SERVICE+VAT:.2f}")
elif 50 <= SERVICE <= 1000:
    VAT = ( SERVICE + BILL ) * ( 7 / 100 )
    print(f"{BILL+SERVICE+VAT:.2f}")
elif SERVICE > 1000:
    SERVICE = 1000
    VAT = ( SERVICE + BILL ) * ( 7 / 100 )
    print(f"{BILL+SERVICE+VAT:.2f}")
