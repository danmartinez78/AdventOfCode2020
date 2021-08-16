import re
input_file = open('test.txt', 'r') 
passports = input_file.read().split('\n\n')
key_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] 
  
# part 1
valid_passports = 0
valid_array = []
for passport in passports:
    passport = passport.replace('\n', ',')
    passport = passport.replace(' ', ',')
    passport = passport.split(',')
    if '' in passport:
        passport.remove('')
    validation = {key: '' for key in key_list} 
    for entry in passport:
        field,value = entry.split(':')
        validation[field] = value
    if all(value != '' for value in validation.values()):
        valid_passports += 1
        valid_array.append(validation)
print(valid_passports)

# part 2
valid_passports = 0
for passport in valid_array:
    has_byr = False
    has_iyr = False
    has_eyr = False
    has_hgt = False
    has_hcl = False
    has_ecl = False
    has_pid = False
    for field in passport:
        value = passport[field]
        if field == 'byr':
            value = int(value)
            if value >= 1920 and value <=2002:
                has_byr = True
        elif field == 'iyr':
            value = int(value)
            if value >= 2010 and value <=2020:
                has_iyr = True
        elif field == 'eyr':
            value = int(value)
            if value >= 2020 and value <=2030:
                has_eyr = True
        elif field == 'hgt':
            unit = value[-2:]
            hgt = value[:-2]
            if unit == 'cm' or  unit == 'in':
                hgt = int(hgt)
            if unit == 'cm' and (hgt >= 150 and hgt <= 193):
                has_hgt = True
            elif unit == 'in' and (hgt >= 59 and hgt <= 76):
                has_hgt = True
        elif field == 'hcl':
            if value[0] == '#' and len(value) == 7:
                if (bool(re.match("^[a-f0-9_-]*$", value[1:]))):
                    has_hcl = True
        elif field == 'ecl':
            if value == 'amb' or value == 'blu' or value == 'brn' or value == 'gry' or value == 'grn' or value == 'hzl' or value == 'oth':
                has_ecl = True 
        elif field == 'pid':
            if len(value) == 9 and bool(re.match("^[0-9_-]*$", value)):
                has_pid = True
    if has_byr and has_iyr and has_eyr and has_hgt and has_hcl and has_ecl and has_pid:
        valid_passports += 1
        # print('GOOD', passport,'\n', has_byr, has_ecl, has_eyr, has_hcl, has_hgt, has_iyr, has_pid, '\n')
    else:
        # print('BAD', passport,'\n', has_byr, has_ecl, has_eyr, has_hcl, has_hgt, has_iyr, has_pid, '\n')
        pass
print(valid_passports)