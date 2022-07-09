import re
def remove_comment(string):
    string = re.sub(r'//.*', '', string)
    string = re.sub(r'/\*.*?\*/', '', string, flags=re.DOTALL)
    return string