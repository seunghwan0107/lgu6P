data = [
    {'name' : '철수', 'math':85, 'eng':90, 'sci':75},
    {'name' : '준호', 'math':73, 'eng':85, 'sci':93},
    {'name' : '영희', 'math':92, 'eng':88, 'sci':90},
]

# dir = {}

# for d in data:
#     name = d['name']
#     total = d['math'] + d['eng'] + d['sci']
#     avg = total/3
#     dir[name] = [total, avg]

# print(dir)
result ={}
for ta in data:
    # total = ta['math']+ta['eng']+ta['sci']
    # avg = total/3
    total = 0
    count = 0
    for k,v in ta.items():
        if k != 'name':
             total += v
             count += 1
    avg = total / count

    result[ ta['name']] = [total,round(avg,4)]

print(result)    


