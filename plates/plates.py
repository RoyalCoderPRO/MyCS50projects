def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    number_mode = False
    integers = ()
    for char in s:
        if type(char).isalpha():
        elif type(char).isnumeric():
            number_mode = True
            integers += int(char)
        if number_mode = True and type(char).isalpha():
            return False
    if char[0] == 0:
        return False

    if s[0].isalpha() and s[1].isalpha() and 2 <= len(s) <= 6:
        return True


main()