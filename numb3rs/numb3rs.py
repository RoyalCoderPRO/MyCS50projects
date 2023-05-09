import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.fullmatch(r"\d+\.\d+\.\d+\.\d+", ip):
        return False
    ips = ip.split('.')
    for i in ips:
        if not 0<= int(i) <= 255:
            return False
    else:
        return True


if __name__ == "__main__":
    main()