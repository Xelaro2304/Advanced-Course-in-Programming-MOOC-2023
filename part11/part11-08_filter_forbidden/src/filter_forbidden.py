# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str) :
    return ''.join([character if character not in forbidden else '' for character in string])