from validator_collection import validators, checkers, errors
def main():
    print(email_checking())

def email_checking():
    email = input("What's your email address? ")
    email_address = validators.email(email)

    try:
        email_address = validators.email(email)
    except:
        pass
    return email_address
main()