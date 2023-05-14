from validator_collection import validators, checkers, errors

def email_checking():
    email = input("What's your email address?")
    email_address = validators.email(email)


    try:
        email_address = validators.email(email)
    except errors.InvalidEmailError:
        # More handlign logic goes here

    is_email_address = checkers.is_email('test@domain.dev')
    # The value of is_email_address will now be True

    is_email_address = checkers.is_email('this-is-an-invalid-email')
    # The value of is_email_address will now be False

    is_email_address = checkers.is_email(None)
    # The value of is_email_address will now be False