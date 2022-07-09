import re

def check_with_data_type(string, data_type):
    if data_type == "int":
        if re.match("-?[0-9]+", string):
            return True
        else:
            return False
    elif data_type == "float":
        if re.match("-?[0-9]+\.[0-9]+", string):
            return True
        else:
            return False
    elif data_type == "char":
        if re.match(".", string):
            return True
        else:
            return False
    elif data_type == "long":
        if re.match("-?[0-9]+", string):
            if int(string) >= -2 ** 63 and int(string) < 2 ** 63:
                return True
        return False
    elif data_type == "ulong":
        if re.match("[0-9]+", string):
            if int(string) < 2 ** 64:
                return True
        return False
    elif data_type == "uint":
        if re.match("[0-9]+", string):
            if int(string) <= 4294967295:
                return True
        return False
    elif data_type == "short":
        if re.match("-?[0-9]+", string):
            if int(string) <= 32767 and int(string) >= -32768:
                return True
        return False
    elif data_type == "ushort":
        if re.match("[0-9]+", string):
            if int(string) <= 65535:
                return True
        return False
    elif data_type == "bool":
        if string in ["true", "false"]:
            return True
        else:
            return False
