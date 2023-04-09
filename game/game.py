import random as rand

while True:
    x = int(input('Level: '))
    if 1 <= x <= 100:
        break
    else:
        pass
y = rand.randint(1,x)
while True:
    z = int(input('Guess: '))
    if z < y:
        print('Too small!')
    if z == y:
        print('Just right!')
        break
    if z > y:
        print('Too large!')