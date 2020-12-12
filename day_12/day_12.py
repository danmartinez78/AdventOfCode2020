import time
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
