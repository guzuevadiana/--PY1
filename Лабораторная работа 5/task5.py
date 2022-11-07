from random import sample
import string


def get_random_password() -> str:
    symbols = string.ascii_lowercase + string.ascii_uppercase + string.digits
    number_of_symbols = 8
    return ''.join(sample(symbols, number_of_symbols))


print(get_random_password())
