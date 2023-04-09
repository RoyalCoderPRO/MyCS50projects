names_list = []

while True:
    try:
        names_list.append(input('Name: ') + ', ')
    except EOFError:
        break
print()
names_list = names_list[-2].replace(',','and')
print(names_list[-2])
if len(names_list) > 2:
    names_list[-1].replace(',','')
names = ''
for name in names_list:
    names += name
print('Adieu, adieu to '+ names)