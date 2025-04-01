
# a = int(input("숫자를 입력하세요: "))
# i = a
# while i > 0:
#     print(i)

#     i -= 1

#     if i == 0 :
#         break

# print("반복 번수: ", )

num = int(input("숫자: "))
if num <= 0:
    print("허허")
else:
    count = 0
    # print(f"while 이전: number: {num},count:{count}")
    while num > 0:
        print(num)
        num -= 1
        count += 1
        # print(f"while 이후: number: {num},count:{count}")
        if num == 0:

         print("반복횟수: ",count)


