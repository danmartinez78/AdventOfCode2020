import time
from collections import deque
import numpy as np
input_file = open('input.txt', 'r')
instructions = input_file.read().split('\n')

def dec_to_bin(n):
    return '{0:036b}'.format(n)

def bin_to_dec(n):
    return int(binary, 2)

def apply_mask(n, mask):
    result = ''
    for i in range(len(mask)):
        if mask[i] != 'X':
            result += mask[i]
        else:
            result += n[i]
    return result

mem= {}

total = 0
for ins in instructions:
    ins = ins.replace(' ', '')
    cmd, val = ins.split('=')
    print(cmd, val)
    if cmd == 'mask':
        mask = val
    else:
        address = cmd
        val = int(ins.split('=')[1])
        binary = dec_to_bin(val)
        binary = apply_mask(binary, mask)
        mem[address] = bin_to_dec(binary)

total = 0
for key in mem.keys():
    total += mem[key]

print(mem)
print(total)



