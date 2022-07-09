import re

def valid_identifier(string):
    if re.match("[a-zA-Z_$][a-zA-Z0-9_$]*", string):
        return True
    else:
        print("Invalid identifier: " + string)
        return False