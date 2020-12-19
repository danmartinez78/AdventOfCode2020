import time
from numpy import where
input_file = open('input.txt', 'r')
numbers = input_file.read().split(',')

target = 2020
mem = {}

print(numbers)
for i in range(len(numbers),target):
    current = numbers[i-1]
    indices = [i for i, x in enumerate(numbers) if x == current]
    if len(indices) < 2:
        numbers.append('0')
    else:
        last = int(indices[-1])
        prev = int(indices[-2])
        numbers.append(str(last-prev))

print(numbers[-1])