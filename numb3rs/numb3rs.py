import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.search(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", ip):
        return False
    ips = ip.split('.')
    elif
    else:
        return True


if __name__ == "__main__":
    main()