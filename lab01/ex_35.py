A = [[1,0,1],
     [0,2,0],
     [1,2,1]]

B = [[2,3,1],
     [0,1,1],
     [1,1,1]]
# 행 i 열 j
#내가한거 고쳐라 , 에라이 븅시나 이것도 못하냐
# C = []
# for i in range(len(A)):
#     total = 0
#     for j in range(len(A[0])):
#        total += A[i][j]
#        print(total)

#        C.append(total)
# print(C)     


############################################
# i :  0        1      2
# j : 0 1 2   0 1 2   0 1 2


A = [[1,0,1],[0,2,0],[1,2,1]]
B = [[2,3,1],[0,1,1],[1,1,1]]
C = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        # print(i,j)
        C[i][j] =  A[i][j] + B[i][j]
print(C)

# temp로 하는방법 물어보셈