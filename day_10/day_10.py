from itertools import combinations
from numpy import sum, min, max, sort, append
import time
input_file = open('test2.txt', 'r')
jolts = input_file.read().split('\n')
jolts = [int(i) for i in jolts]
jolts = sort(jolts)

start_time = time.time()

# part 1

adapter = max(jolts) + 3
jolts = append(jolts, adapter)
current = 0
one_off = 0
three_off = 0
for rating in jolts:
    diff = rating - current
    if diff == 1:
        one_off += 1
    elif diff == 3:
        three_off += 1
    current = rating

print('part one')
print('answer:', one_off*three_off)
print('time:', time.time() - start_time)

# part 2

def recurse(jolts, current, count, adapter):
    if current == adapter:
        return 1
    elif current not in jolts:
        return 0
    else:
        success = 0
        for delta in [1,2,3]:
            result = recurse(jolts, current+delta, count, adapter)
            if result > 0:
                success += result
        return count + success

start_time = time.time()
jolts = append([0], jolts)
adapter = max(jolts)
print('part two: recursion')
print('answer', recurse(jolts[:-1], 0, 0, adapter))
print('time:', time.time() - start_time)

# part 2 better

def recurse2(jolts, current, count, adapter, good):
    if current == adapter:
        return 1, good
    elif current in good.keys():
        return good[current], good
    elif current not in jolts:
        return 0, good
    else:
        success = 0
        for delta in [1,2,3]:
            result, good = recurse2(jolts, current+delta, count, adapter, good)
            if result > 0:
                if current+delta not in good:
                    good[current+delta] = result
                success += result
        return count + success, good

start_time = time.time()
jolts = append([0], jolts)
adapter = max(jolts)
print('part two: recursion with memoization')
print('answer:', recurse2(jolts[:-1], 0, 0, adapter, {})[0])
print('time:', time.time() - start_time)