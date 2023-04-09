names = []

while True:
    try:
        names.append(input('Name: ') + ',')
    except EOFError:
        break
names[-1].replace(',','')
names[-2].replace(',','and')
print('Adieu, adieu to, )