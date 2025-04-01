L = [1,2,3,4,5]
# i in 다음에 시퀀스형자료 들어올수 있음
for i in range(len(L)):
    print('index: ',i)
    print('L[i]: ',L[i])
    print(i)


for j in L:
    print(j)

D = {'A':100, 'B':200, 'C':300}
print(D.items())
#dict_items(
#    [('A':100) , ('B':200), ('C':300)]
# )

# for k,v in D.items():
for k,v in [('A',100) , ('B',200), ('C',300)]:
    print(k,v)