import random

def main():
    generate_integer(get_level())

def get_level():
    while True:
        try:
            l = int(input())
            assert l == 1 or l == 2 or l == 3
        except (ValueError,AssertionError):
            continue
        else:
            print('level: ' + str(l))
            return l

def generate_integer(l):
    counter = 0
    score = 0
    while counter < 10:
        if l == 1:
            x = random.randint(0, 10**(l)-1)
            y = random.randint(0, 10**(l)-1)
        else:
            x = random.randint(10**(l-1), 10**(l)-1)
            y = random.randint(10**(l-1), 10**(l)-1)
        print(str(x) +' + ' + str(y) + ' = ', end='')
        z = x + y
        ans = int()
        tries = 1
        while tries <= 3 and ans != z:
            tries += 1
            ans = int(input())
            if ans != z:
                print('EEE')
        if ans != z:
            print(z)
        else:
            score += 1
        counter += 1
    print(score)

if __name__ == "__main__":
    main()
