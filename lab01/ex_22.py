# n = int(input("자연수를 입력하세요: "))
# totall = 0
# for i in range(1,n+1):
    
#     count = 0
#     i = 1
  
#     while n >0:
#         count += 1
#         n += 1

#         totall += i
        

# print(f"1부터 {n}까지의 합은 {totall}입니다.")

n = int(input("n :"))

s = 0

for i in range(1, n+1):
    print(f"합산전 s:{s},i:{i}")
    s = s + i
    print(f"합산후 s:{s},i:{i}")
    print("======================")
    print(s)



