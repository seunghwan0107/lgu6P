X = [[78, 80, 95, 55, 67, 43],[45, 67, 90, 87, 88, 93]]

def mean(l):
    S = 0
    for x_k in l:
        S += x_k
        N = len(l)
        m = S / N
        
       
        return m

for x in X:
    m = mean(x)
    print(m)

AVG = [round(mean(x),2) for x in X]

# m = mean(X[0])
# print(m)

# AVG=[]
# for x in X:
#     m = mean(x)
#     #print(m)
#     AVG.append(round(m,2))
print(AVG)