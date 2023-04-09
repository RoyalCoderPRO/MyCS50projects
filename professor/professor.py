import random

while True:
    try:
        l = int(input())
        assert l == 1 or l == 2 or l == 3
        break
    except AssertionError:
        pass
x = random.randint(0, 10**(l-1))
y = random.randint(0, 10**(l-1))
z = x + y

tries = 1
while tries <= 3 and ans != z:
    tries += 1
    ans = input()
    print('EEE')
if ans != z:
    print(z)
elif:
