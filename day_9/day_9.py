from itertools import combinations
from numpy import sum, min, max
import time
input_file = open('input.txt', 'r')
numbers = input_file.read().split('\n')
numbers = [int(i) for i in numbers]


start_time = time.time()

# part 1
preamble_size = 25
preamble = numbers[0:preamble_size]
bad_number = 0
for i in range(preamble_size,len(numbers)):
    combos = [sum(c) for c in combinations(preamble, 2)]
    number = numbers[i]
    if number not in combos:
        bad_number = number
        print(number)
        break
    else:
        preamble.append(number)
        preamble.pop(0)

# part 2
for i in range(len(numbers)):
    j = i + 1
    found = False
    while not found:
        j += 1
        arr = numbers[i:j]
        psum = sum(arr)
        if psum == bad_number:
            print(min(arr) + max(arr))
            found = True
            break
        elif psum > bad_number:
            break
    if found:
        break

