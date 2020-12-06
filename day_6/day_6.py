from numpy import sum
input_file = open('input.txt', 'r') 
answer_groups = input_file.read().split('\n\n')

# part 1
counts = []
for group in answer_groups:
    group = group.split('\n')
    questions = []
    for answer in group:
        for q in answer:
            if q not in questions:
                questions.append(q)
    counts.append(len(questions))
print(sum(counts))

# part 2
counts = []
for group in answer_groups:
    group = group.split('\n')
    req = len(group)
    questions = {}
    for answer in group:
        for q in answer:
            if q not in questions.keys():
                questions[q] = 1
            else:
                questions[q] += 1
    count = 0
    for q in questions.keys():
        if questions[q] == req:
            count += 1
    counts.append(count)
print(sum(counts))