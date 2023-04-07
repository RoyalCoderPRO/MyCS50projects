def main():
    convert()

def convert():
    str = input().replace(':)','🙂')
    str = str.replace(':(','🙁')
    print(str)
    return str
main()