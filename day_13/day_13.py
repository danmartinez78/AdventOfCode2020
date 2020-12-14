import time
from collections import deque
import numpy as np
input_file = open('input.txt', 'r')
data = input_file.read().split('\n')

depart_time = int(data[0])
busses = [int(i) if i != 'x' else 'x' for i in data[1].split(',')]
bus_ids = list(filter(lambda i: i != 'x', busses))

start_time = time.time()

# part 1

min_wait = 1000000
best_bus = 0
for bus in bus_ids:
    wait = (int(depart_time/bus)*bus + bus) - depart_time
    if wait < min_wait:
        min_wait = wait
        best_bus = bus
print(best_bus*min_wait)

# part 2

offsets = [0]
for i in range(1,len(busses)):
    if busses[i] == 'x':
        pass
    else:
        offsets.append(i)

ids = []
for bus in busses:
    if bus != 'x':
        ids.append(bus)
t = 0
i = 1
delta = ids[i-1]
found = False
while not found:
    t += delta
    mods = []
    for j in range(len(ids)):
        mods.append((t+offsets[j])%ids[j])
    print('t:', t, 'mods:', mods)
    if (t+offsets[i])%ids[i] == 0:
        delta *= ids[i]
        i += 1
    if i >= len(ids):
        print(t)
        found = True

