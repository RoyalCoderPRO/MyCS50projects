x = 0
a_p = 0
while a_p < 50:
    print('Amount Due: ' + str(50 - a_p))
    x = int(input('Insert Coin: '))
    if x != 5 and x != 10 and x != 25:
        continue
    else:
        a_p += x
if a_p >= 50:
    print('Change Owed: ' + str(a_p - 50))