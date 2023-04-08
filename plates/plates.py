def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    number_mode = False
    for char in s:
        if type(char) is int:
            number_mode = True
        if number_mode == True:
            
        if number_mode == True and type(char) is str:
            return False
    if s[0].isalpha() and s[1].isalpha() and 2 <= len(s) <= 6:
        return True


main()