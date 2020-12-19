import time
from numpy import sum
input_file = open('input.txt', 'r')
data = input_file.read()
data = data.replace(' ', '')
restrictions, my_ticket, nearby_tickets = data.split('\n\n')
restrictions = restrictions.split('\n')
nearby_tickets = nearby_tickets.split('\n')[1:]

for i in range(len(nearby_tickets)):
    ticket = nearby_tickets[i]
    ticket = ticket.split(',')
    nearby_tickets[i] = [int(i) for i in ticket]

rules = {}
for r in restrictions:
    desc, values = r.split(':')
    low, high = values.split('or')
    low = [int(n) for n in low.split('-')]
    high = [int(n) for n in high.split('-')]
    rules[desc] = (low, high)

errors = []
for ticket in nearby_tickets:
    for value in ticket:
        error = True
        for key in rules.keys():    
            for pair in rules[key]:
                if value >= pair[0] and value <= pair[1]:
                    error = False
        if error:
            errors.append(value)

print(sum(errors))
