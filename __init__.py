from src.verilogGenerator.remove_white_space import remove_white_space
from src.verilogGenerator.remove_comment import remove_comment


file = open("/home/dj/vegg-c-v/examples/kernel.cl", "r")
string = file.read()
file.close()
print(string)

print(remove_white_space(remove_comment(string)))