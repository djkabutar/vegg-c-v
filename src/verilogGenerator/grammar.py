import re
from remove_comment import remove_comment
from remove_white_space import remove_white_space
from separator import stack
from identifiers import valid_identifier
from keywords import get_all_keyword

def check_grammar(string):
    string = remove_white_space(remove_comment(string))
    print(string)

    if len(stack) == 0:
            i = 0         
            while string[i] == " " and len(string[i:]) > 1:
                i += 1

            if string[i: i+8] == "__kernel":
                i += 8
                if string[i] != " ":
                    print("Error at line " + str(i) + ": __kernel must be followed by a space")
                    return False

                i += 1

                i = white_space(i, string)
                 
                if string[i: i+4] != "void":
                    return False

                i += 4

                if string[i] != " ":
                    print("Error at line " + str(i) + ": void must be followed by a space")
                    return False
                
                i += 1

                i = white_space(i, string)

                prevI = i
                while string[i] != "(" and string[i] != " " and len(string[i:]) > 1:
                    i += 1

                if not valid_identifier(string[prevI: i]):
                    return False
                else:
                    print(string[prevI: i])

                while string[i] == " " and len(string[i:]) > 1:
                    i += 1

                if string[i] != "(":
                    print("Error at line " + str(i) + ": ( must be followed by a space")
                    return False
                
                i += 1

                i = white_space(i, string)
                
                if not re.match("\)",string[i]):
                    temp = i
                    while string[temp] != ")" and len(string[temp:]) > 1:
                        temp += 1
                    
                    parameter = string[i: temp].split(",")

                    for param in parameter:
                        j = 0
                        print(param)
                        j = white_space(j, param)

                        for keyword in get_all_keyword():
                            if param[j: j+len(keyword)] == keyword:
                                break

                            # print(param[j: len(keyword)], " = ", keyword)

                        j = white_space(j, param)

                        if not valid_identifier(param[j:]):
                            return False
                    
                    i = temp
                    if string[i] != ")":
                        print("Error at line " + str(i) + ": ) must be followed by a space")
                        return False

            # if string[13] != " ":
        
            # else:
            #     for keyword in get_all_keyword():
            #         if string[0:len(keyword)] == keyword:
            #             if string[len(keyword)] != " ":
            #                 return False
                        
            #             break

    return True

def white_space(i, string):
    while string[i] == " " and len(string[i:]) > 1:
        i += 1
    return i

if __name__ == "__main__":
    file = open("/home/dj/vegg-c-v/examples/kernel.cl", "r")
    string = file.read()
    file.close()
    if check_grammar(string) :
        print("Valid Syntax")
    else:
        print("Invalid Syntax")
