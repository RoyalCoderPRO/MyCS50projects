name = input()
new_name = ('')
for letter in name:
    if letter.isupper():
        letter.append('_')
    new_name.append(letter)
