from validator_collection import validators, checkers, errors

email_address = validators.email('test@domain.dev')
# The value of email_address will now be "test@domain.dev"

email_address = validators.email('this-is-an-invalid-email')
# Will raise a ValueError

try:
    email_address = validators.email(None)
    # Will raise an EmptyValueError
except errors.EmptyValueError:
    # Handling logic goes here
except errors.InvalidEmailError:
    # More handlign logic goes here

email_address = validators.email(None, allow_empty = True)
# The value of email_address will now be None

email_address = validators.email('', allow_empty = True)
# The value of email_address will now be None

is_email_address = checkers.is_email('test@domain.dev')
# The value of is_email_address will now be True

is_email_address = checkers.is_email('this-is-an-invalid-email')
# The value of is_email_address will now be False

is_email_address = checkers.is_email(None)
# The value of is_email_address will now be False