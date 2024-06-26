
def balanced_brackets(my_string: str):
    brackets ='()[]'
    my_string = ''.join([character for character in my_string if character in brackets])
    if len(my_string) == 0:
        return True
    if len(my_string) % 2 != 0:
        return False
    if my_string[0] == '(' or my_string[0] == '[':
        if my_string[-1] == ')' or my_string[-1] == ']':
            if not ((my_string[0] == '(' and my_string[-1] == ')') or (my_string[0] == '[' and my_string[-1] == ']')):
                return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])
