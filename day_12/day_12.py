import time
from collections import deque
import numpy as np
input_file = open('input.txt', 'r')
commands = input_file.read().split('\n')

start_time = time.time()

# part 1

def move(x, y, direction, value):
    if direction == 'E':
        y += value
    elif direction == 'W':
        y -= value
    elif direction == 'N':
        x += value
    elif direction == 'S':
        x -= value
    return x, y

def rotate(rot, value):
    directions = ['E', 'S', 'W', 'N']
    rot += value
    if rot >= 360:
        rot -= 360 # could modulo to wrap instead
    elif rot < 0:
        rot += 360
    index = int(rot/90)
    direction = directions[index]
    return rot, direction

x = 0 # + in north
y = 0 # + in east
rot = 0 # east
direction = 'E'
i = 0
for command in commands:
    cmd = command[0]
    value = int(command[1:])
    i += 1
    if cmd == 'R':
        rot, direction = rotate(rot, value)
    elif cmd == 'L':
        rot, direction = rotate(rot, -value)
    elif cmd == 'F':
        x,y = move(x, y, direction, value)
    else:
        x,y = move(x, y, cmd, value)
dist = abs(y) + abs(x)
print(y, x, dist)

# prt 2

def move_wp(wp, direction, value):
    if direction == 'E':
        wp[0] += value
    elif direction == 'S':
        wp[1] += value
    elif direction == 'W':
        wp[2] += value
    elif direction == 'N':
        wp[3] += value
    return wp

def rot_wp(wp, value):
    # shift direction array value/90 times fwd or back
    shift = int(value/90)
    wp.rotate(shift)
    return wp, pos

def move_to_wp(pos,wp,N):
    for i in range(N):
        pos += np.asarray(wp)
    return deque(pos)

wp = deque([10,0,0,1])
pos = deque([0,0,0,0])
directions = ['E', 'S', 'W', 'N']

i = 0
for command in commands:
    cmd = command[0]
    value = int(command[1:])
    i += 1
    if cmd == 'F':
        pos = move_to_wp(pos, wp, value)
    elif cmd == 'R':
        wp, pos = rot_wp(wp, value)
    elif cmd == 'L':
        wp, pos = rot_wp(wp, -value)
    else:
        wp = move_wp(wp, cmd, value)

print(pos, dist)
print(abs(pos[0]-pos[2])+abs(pos[1]-pos[3]))


