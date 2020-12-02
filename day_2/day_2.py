input_file = open('input.txt', 'r') 
lines = input_file.readlines() 
  

# part 1
valid_passwords = 0
for line in lines: 
    # print("{}".format(line.strip()))
    minimum, maximum = line.split()[0].split('-')
    letter = line.split()[1][0]
    password = line.split()[2]
    # print(minimum, maximum, letter, password)
    letter_count = 0
    for c in password:
        if c == letter:
            letter_count += 1
    if letter_count >= int(minimum) and letter_count <= int(maximum):
        valid_passwords += 1
print(valid_passwords)

# part 2
valid_passwords = 0
for line in lines: 
    # print("{}".format(line.strip()))
    index_1, index_2 = line.split()[0].split('-')
    index_1 = int(index_1) - 1
    index_2 = int(index_2) - 1
    letter = line.split()[1][0]
    password = line.split()[2]
    if password[index_1] == letter and password[index_2] == letter:
        pass
    elif password[index_1] == letter or password[index_2] == letter:
        valid_passwords += 1
print(valid_passwords)