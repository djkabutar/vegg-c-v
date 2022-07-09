def get_all_operators():
    return ['+', '-', '*', '/', '%', '^', '&', '|', '~', '<<', '>>', '==', '!=', '<', '>', '<=', '>=', '&&', '||', '!', '?', ':', '=', '+=', '-=', '*=', '/=', '%=', '^=', '&=', '|=', '<<=', '>>=', '++', '--', ',']

def check_valid_operator(string):
    if string in get_all_operators():
        return True
    else:
        print("Invalid operator: " + string)
        return False
