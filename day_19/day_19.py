import time
import copy
from numpy import sum
fn = 'test.txt'
input_file = open(fn, 'r')
data = input_file.read()
rules, messages = data.split('\n\n')
rules = rules.split('\n')
messages = messages.split('\n')
print(rules, messages)
