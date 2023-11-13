import re

def check_email(email, regex):
    pattern = re.compile(regex)
    return bool(pattern.match(email))

# Example usage
regex_pattern = r"^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$"
email_to_check = 'example@email.com'

if check_email(email_to_check, regex_pattern):
    print(f'The email "{email_to_check}" is valid.')
else:
    print(f'The email "{email_to_check}" is not valid.')