name = input()
new_name = ('')
for letter in name:
    if letter.isupper():
        new_name.append('_')
    new_name.append(letter)
