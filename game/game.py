import random as rand

while True:
    try:
        x = int(input('Level: '))
    except ValueError:
        pass
    else:
        if 1 <= x <= 100:
            break
        else:
            pass
y = rand.randint(1,x)
while True:
    try:
        z = int(input('Guess: '))
    except ValueError:
        pass
    else:
        if z < y:
            print('Too small!')
        if z == y:
            print('Just right!')
            break
        if z > y:
            print('Too large!')