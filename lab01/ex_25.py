# PW = 1234


# for i in range(5):
#     ps = int(input("비밀번호를 입력하세요: "))

#     if ps == PW:
#         print("로그인")
#         break
    
#     else:
#         print("다시 입력하세요 ")

# else:
#     print("로그인을 잠구겠습니다.")


     
password = "1234"
success = False

for t in range(5):
    user_pw = input("PW: ")

    if user_pw == password:
        print("로그인 성공")
        success = True
        break
    else:
        print("다시 입력하세요.")

if success == False:
    print("잠금")