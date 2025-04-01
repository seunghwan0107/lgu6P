import pandas as pd

df = pd.read_excel("./data/scores.xlsx")

print(df,type(df))

print(df.T.to_dict())
# T는 데이터를 90도 돌려서 나오게 하는거

data = [v for k, v in df.items()]
print(data)

result ={}
for ta in data:
    # total = ta['math']+ta['eng']+ta['sci']
    # avg = total/3
    total = 0
    count = 0
    for k,v in ta.items():
        if k != 'name':
             total += ta
             count += 1
    avg = total / count

    result[ ta['name']] = [total,round(avg,4)]

print(result)    