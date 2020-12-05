from math import ceil, floor
from numpy import max
input_file = open('input.txt', 'r') 
seat_assignments = input_file.readlines()
  
# part 1
# bisect row then col then row*8+col
seat_ids = []
for seat_partition in seat_assignments:
    row_min = 0
    row_max = 127
    # print(row_min, row_max)
    for indicator in seat_partition[:6]:
        if indicator == 'F':
            row_max = row_min + floor((row_max - row_min)/2)
        else:
            row_min = row_min + ceil((row_max - row_min)/2)
        # print(indicator, row_min, row_max)
    if seat_partition[6] == 'F':
        final_row = row_min
    else:
        final_row = row_max
    col_min = 0
    col_max = 7
    # print(col_min, col_max)
    for indicator in seat_partition[7:9]:
        if indicator == 'L':
            col_max = col_min + floor((col_max - col_min)/2)
        else:
            col_min = col_min + ceil((col_max - col_min)/2)
        # print(indicator, col_min, col_max)
    if seat_partition[9] == 'R':
        final_col = col_max
    else:
        final_col = col_min
    # print('row:', final_row, 'col:', final_col)
    seat_ids.append(final_row*8 + final_col)
print(max(seat_ids))

# part 2
# shitty brute force
for i in range(max(seat_ids)):
    if i in seat_ids:
        continue
    ahead = False
    behind = False
    for other_seat in seat_ids:
        if other_seat == i + 1:
            ahead = True
        elif other_seat == i - 1:
            behind = True
    if ahead and behind:
        print(i)
