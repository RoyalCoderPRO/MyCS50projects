x = input('Type something here: ')
y = ('')
for l in x:
    if l.lower() == 'a' or l.lower() == 'e' or l.lower() == 'i' or l.lower() == 'o' or l.lower() == 'u':
        continue
    else:
        y += l
print(y)