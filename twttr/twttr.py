def main():

    x = input('Type something here: ')

    shorten(x):

def shorten(word):

    y = ('')
    for l in word:
        if l.lower() == 'a' or l.lower() == 'e' or l.lower() == 'i' or l.lower() == 'o' or l.lower() == 'u':
            continue
        else:
            y += l
    return(y)

if __name__ == "__main__":
    main()