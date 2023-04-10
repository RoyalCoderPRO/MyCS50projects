def main():

    print(shorten())

def shorten(word='Twitter'):

    y = ('')
    for l in word:
        if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
            continue
        else:
            y += l
    return(y)

if __name__ == "__main__":
    main()