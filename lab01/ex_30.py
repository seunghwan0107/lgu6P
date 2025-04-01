# n =5
# for i in range(n):

#     for j in range(5-i):
#         print(' ',end='')

#     for k in range(2*i+1):
#         print('*',end ='')
#     print()

# n = 5
    
# for i in range(n):
  
#     for j in range(n-i-1):
#        print(' ',end='')#공백
    
#     for k in range(i*2+1):   #별
#        print('*',end='')
#     print()

n = 5
for i in range(n):
    print(f"{'*' * (i*2+1):^{2*n-1}}")