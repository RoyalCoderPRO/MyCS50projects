name = input('Type something here: ')
new_name = ('')
for letter in name:
    if letter.isupper():
        new_name += '_'
    new_name += letter.lower()
print(new_name)
