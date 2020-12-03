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
