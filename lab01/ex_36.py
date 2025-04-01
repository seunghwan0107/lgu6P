# a = [1,2,3,4]
# b = [4,5,6,7]
# c = ai*bi
# c = 0

# # for i in range(len(a)):
# #     print(len(a))
# #     for j in range(len(a[0])):

# for i in range(len(a)):
#     c+= a[i]*b[i]
   
# print(c)
#######################################################
#  j  0 1 2   0 1 2   0 1 2
#  A : (3,3) B : (3,3)
A = [[1,0,1],
     [0,2,0],
     [1,2,1]]
B = [[2,3,1],
     [0,1,1],
     [1,1,1]]
C = [[0,0,0],
     [0,0,0],
     [0,0,0]]

# for i in range(3):
#     d=[]
#     for j in range(3):
#         c=0
#         for k in range(3): 
#             # A[i][k] B[k][j]
#             c+= A[i][k] * B[k][j]
#         d.append(c)
#     C.append(d)
    
# print(C)
# ###################################################   
#  A(3,3) B(3,3) C(3,3) 일때
# for i in range(len(A)):
#     for j in range(len(B[0])):
#         # A의 i행과 B의 j행을 내적
#         for k in range(len(A[0])):
#             C[i][j] += A[i][k]*B[k][j]
# print(C)            

#   A(3,4) B(4,2) C(3,2)


A = [[1,0,1,6],
     [0,2,0,4],
     [1,2,1,6]]

B = [[2,3],
     [0,1],
     [1,1],
     [2,5]]


C = [[0,0],
     [0,0],
     [0,0]]


row = len(A)
col = len(B[0])

C = []

for i in range(row):
    temp = []
    for j in range(col):
        temp.append(0)
    C.append(temp)
#  C = [[0,0],
#      [0,0],
#      [0,0]]

    for k in range(len(A[0])):
            C[i][j] += A[i][k]*B[k][j]
print(C)



        