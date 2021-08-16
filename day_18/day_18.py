import re
import pyparsing
input_file = open('test.txt', 'r')
data = input_file.read()
data = data.replace(' ', '')
problems = data.split('\n')

def process(p):
    val = 0
    i = 0
    while i < len(p):
        c = p[i]
        if c == '+':
            i += 1
            val += int(p[i])
            i += 1
        elif c == '*':
            i += 1
            val *= int(p[i])
            i += 1
        else:
            val = int(p[i])
            i += 1
    return val


running_sum = 0
for p in problems:
    print(p)
    print(process(p))
