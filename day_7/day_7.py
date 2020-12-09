import time

input_file = open('input.txt', 'r')
rules = input_file.read().split('\n')

start_time = time.time()
# part 1
def check_bag(bags, bag, d = 0):
    #print(d, bag)
    if bag[0] == 'shiny gold':
        return True
    elif len(bags[bag[0]]) > 0:
        for contents in bags[bag[0]]:
            if check_bag(bags, contents, d+1):
                return True
    else:
        return False   
# part 2
def sum_bags(bags, bag, d = 0, count = 0):
    # print(d, bag, count)
    color = bag[0]
    amt = bag[1]
    if len(bags[color]) == 0:
        return amt
    else:
        inner_bags = 0
        for bag in bags[color]:
            inner_bags += amt*sum_bags(bags, bag, d+1, count)
        return count + amt + inner_bags
# setup
bags = {}
for rule in rules:
    bag, contents = rule.split('contain')
    bag = bag.split(' ')
    bag = bag[0] + ' ' + bag[1]
    if ',' in contents:
        contents = contents.split(',')
    else:
        contents = [contents]
    # print(bag, ':', contents)
    bags[bag] = []
    for content in contents:    
        if content == ' no other bags.':
            pass
        else:
            content = content.split(' ')
            amt = int(content[1])
            color = content[2] + ' ' + content[3]
            bags[bag].append((color, amt))

# for key in bags.keys():
#     print(key, ':', bags[key])

count = 0
for bag in bags.keys():
    if bag == 'shiny gold':
        continue
    if check_bag(bags, (bag, 0)):
        count += 1

print(count)
print(sum_bags(bags, ('shiny gold', 1), 0, 0)-1)
print('time taken:', time.time() - start_time)
