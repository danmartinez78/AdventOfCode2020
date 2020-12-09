import copy
import time
input_file = open('input.txt', 'r')
instructions = input_file.read().split('\n')

start_time = time.time()

# setup and part 1
acc = 0
history = []
i = 0
while i < len(instructions):
    if i in history:
        break
    instruction = instructions[i]
    history.append(i)
    cmd, value = instruction.split(' ')
    value = int(value)
    # print(cmd, value)
    if cmd == 'nop':
        i += 1
    elif cmd == 'acc':
        acc += value
        i += 1
    elif cmd == 'jmp':
        i += value
print(acc)

# part 2
def run(instructions, i, acc, history, static):
    if i in history:
        return False, acc, i, history
    elif i == len(instructions):
        return True, acc, i, history
    history.append(i)
    instruction = instructions[i]
    cmd, value = instruction.split(' ')
    value = int(value)
    # print(i, cmd, value)
    if cmd == 'acc':
        acc += value
        i += 1
        return run(instructions, i, acc, history, static)
    elif cmd == 'nop':
        if not static:
            # try jmp
            # print('trying jmp instead')
            sim_i = i + value
            sim_history = copy.copy(history)
            sim_acc = copy.copy(acc)
            static = True
            results = run(instructions, sim_i, sim_acc, sim_history, static)
            if results[0]:
                return results
            else:
                # print("switch failed continuing as normal")
                static = False
        # run nop
        i += 1
        return run(instructions, i, acc, history, static)
    elif cmd == 'jmp':
        if not static:
            # try nop
            # print('trying nop instead')
            sim_i = i+1
            sim_history = copy.copy(history)
            sim_acc = copy.copy(acc)
            static = True
            results = run(instructions, sim_i, sim_acc, sim_history, static)
            if results[0]:
                return results
            else:
                # print("switch failed continuing as normal")
                static = False
        # run jmp
        i += value
        return run(instructions, i, acc, history, static)

start_instruction = instructions[0]
start_cmd, start_value = start_instruction.split(' ')
start_value = int(start_value)
print(run(instructions, 0, 0, [], False)[1])
print('time taken:', time.time() - start_time)