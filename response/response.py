from validator_collection import validators, checkers, errors
def main():
    print(email_checking())

def email_checking():
    email = input("What's your email address? ")

    try:
        email_address = validators.email(email)
        return 'Valid'
    except (errors.EmptyValueError, errors.InvalidEmailError):
        return 'Invalid'

main()