import numpy as np
import copy
import time

def read_seats(fn):
    input_file = open(fn, 'r')

    seats = input_file.read().split('\n')
    seat_map = []

    for row in seats:
        row = row.replace('.', '0')
        row = row.replace('L', '1')
        row = row.replace('#', '2')
        row = [int(i) for i in row]
        seat_map.append(row)

    seat_map = np.array(seat_map)
    return seat_map
        
def print_seats(seats):
    print('printing seats....\n')
    for row in seats:
        char_row = ''
        for seat in row:
            if seat == 2:
                char_row += '#'
            elif seat == 1:
                char_row += 'L'
            else:
                char_row += '.'
        print(char_row)
    print('\n')

def test_seats(seats, part, num):
    test = read_seats('part_' + str(part) +'/' + str(num) + '.txt')
    if np.array_equal(seats, test):
        print(str(num), 'pass')
    else:
        print(str(num), 'fail')
        print_seats(test)
        print_seats(seats)

# part 1

seats = read_seats('input.txt')
# print(seats[0:2,0:2])
rows, cols = seats.shape
occupied = np.zeros_like(seats)
temp_occ = copy.copy(occupied)
done = False
i = 0
while not done:
    for r in range(rows):
        for c in range(cols):
            seat = seats[r,c]
            if seat == 1:
                rmin = max(0, r-1)
                rmax = min(rows-1, r+1)
                cmin = max(0, c-1)
                cmax = min(cols-1, c+1)
                window = occupied[rmin:rmax+1, cmin:cmax+1]
                if np.sum(window)-occupied[r,c] <= 0:
                    temp_occ[r,c] = 1
    
    if np.array_equal(temp_occ, occupied):
        print(occupied)
        print(temp_occ)
        done = True
        occupied = copy.copy(temp_occ)
        break
    else:
        i += 1
        occupied = copy.copy(temp_occ) 
        # test_seats(occupied+seats, 1, i)
        
    for r in range(rows):
        for c in range(cols):
            seat = seats[r,c]
            if seat == 1:
                rmin = max(0, r-1)
                rmax = min(rows-1, r+1)
                cmin = max(0, c-1)
                cmax = min(cols-1, c+1)
                window = occupied[rmin:rmax+1, cmin:cmax+1]
                if np.sum(window)-1 >= 4:
                    temp_occ[r,c] = 0
    
    if np.array_equal(temp_occ, occupied):
        done = True
        occupied = copy.copy(temp_occ)
        break
    else:
        i += 1
        occupied = copy.copy(temp_occ) 
        # test_seats(occupied+seats, 1, i)

print(np.sum(occupied))

# part 2
rows, cols = seats.shape
occupied = np.zeros_like(seats)
temp_occ = copy.copy(occupied)
done = False
i = 0
while not done:
    for r in range(rows):
        for c in range(cols):
            seat = seats[r,c]
            if seat == 1:
                directions = [[0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1]]
                free = True
                for dr, dc in directions:
                    r_t = r
                    c_t = c
                    filled_chair = False
                    r_t += dr
                    c_t += dc
                    while r_t < rows and r_t >= 0 and c_t < cols and c_t >=0 and filled_chair == False:
                        if (r_t == r and c_t == c):
                            break
                        check = occupied[r_t,c_t] + seats[r_t, c_t]
                        if check == 2:
                            filled_chair = True
                            free = False
                        if check == 1:
                            break
                        r_t += dr
                        c_t += dc
                    if filled_chair:
                        break
                if free:
                    temp_occ[r,c] = 1
    
    if np.array_equal(temp_occ, occupied):
        done = True
        occupied = copy.copy(temp_occ)
        break
    else:
        i += 1
        occupied = copy.copy(temp_occ) 
        # test_seats(occupied+seats, 2, i)
        
    for r in range(rows):
        for c in range(cols):
            seat = seats[r,c]
            if seat == 1:
                directions = [[0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1]]
                free = True
                count = 0
                for dr, dc in directions:
                    r_t = r
                    c_t = c
                    filled_chair = False
                    r_t += dr
                    c_t += dc
                    while r_t < rows and r_t >= 0 and c_t < cols and c_t >=0 and filled_chair == False:
                        if (r_t == r and c_t == c):
                            break
                        check = occupied[r_t,c_t] + seats[r_t, c_t]
                        if check == 2:
                            filled_chair = True
                            count += 1
                        if check == 1:
                            break
                        r_t += dr
                        c_t += dc
                if count > 4:
                    temp_occ[r,c] = 0
    
    if np.array_equal(temp_occ, occupied):
        done = True
        occupied = copy.copy(temp_occ)
        break
    else:
        i += 1
        occupied = copy.copy(temp_occ) 
        # test_seats(occupied+seats, 2, i)

print(np.sum(occupied))