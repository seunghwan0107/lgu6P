# def mean(l):
#     #l 안에 숫자들의 평균
#     total = 0
#     count = 0
#     for number in l:
#         total += number
#         count += 1
        

#     return total / count
   

# avg = mean([2,1,5])
# print(avg)


# def mean(l):
#     #l:List[int|float]
#     n = len(l)
#     s = sum(l)

#     m = s/n

#     return m

# m = mean([1,2,3])
# print(m)

def mean(l):
    S = 0
    for x_k in l:
        S += x_k

    # for k in range(len(l)):
    #     x_k = l[k]
    #     S += x_k

        N = len(l)
        m = S / N
        
        return m
    
avg = mean({1,2,3,4,5,6,})
print(avg)
