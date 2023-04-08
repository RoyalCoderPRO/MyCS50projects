def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    number_mode = False
    integers = ''
    for char in s:
        if char.isalpha():
            pass
        elif char.isnumeric():
            number_mode = True
            integers += char
        else:
            return False
        if number_mode == True and char.isalpha():
            return False
    if number_mode == True:
        if integers[0] == '0':
            return False
    if  2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            return True
        else:
            return False
    return False

main()