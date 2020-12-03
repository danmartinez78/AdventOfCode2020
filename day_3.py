input_file = open('input.txt', 'r') 
lines = input_file.readlines() 
  
# part 1
# track pos, increment pos + 3 every line and increment trees if char is a #
# make sure to wrap x 
pos = 0
num_trees = 0
for line in lines:
    if line[pos] == '#':
        num_trees += 1
    pos = pos + 3
    pos = pos%(len(line)-1)
print(num_trees)

# part 2
pos = 0
num_trees = 0
num_lines = 0
line_array = []
for line in lines:
    num_lines += 1 # probably better way to do this
    line_array.append(line)

dx_values = [1, 3, 5, 7, 1]
dy_values = [1, 1, 1, 1, 2]
tree_array = []

for dx, dy in zip(dx_values, dy_values):
    x = 0
    num_trees = 0
    for y in range(0, num_lines, dy):
        line = line_array[y] 
        if line[x] == '#':
            num_trees += 1
        x += dx
        x = x%(len(line)-1)
    tree_array.append(num_trees)
print(*tree_array)
print(tree_array[0] * tree_array[1] * tree_array[2] * tree_array[3] * tree_array[4]) # lazy lol