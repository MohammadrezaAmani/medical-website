import secrets
import string


def random_password_generator():
    """
    Generates a random password consisting of 9 lowercase letters, one uppercase letter, and one digit.

    Returns:
        str: A randomly generated password.
    """
    password = ""
    for _ in range(9):
        password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    return password
