PW = 1423


# while PW != input("비밀번호를 입력하세요: "):
#     print("다시 입력하세요")

# print("성공") 

while True:
    user_pw = input("PW: ")

    if PW == user_pw:
        print('로그인 성공')
        break
    else:
        print("패스워드가 틀립니다.")
