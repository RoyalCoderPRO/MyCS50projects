names = []

while True:
    try:
        names.append(input('Name: ') + ',')
    except EOFError:
        break
names[-2].replace(',','and')
if len(names) > 2:
    names[-1].replace(',','')
print('Adieu, adieu to, '  )