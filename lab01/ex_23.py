# Id = "seunghwan"
# passwd =1234

# name = str(input("아이디를 입력하세요: "))

# if name != Id:
#     print("그런 아이디는 존재하지 않습니다.")


# else:
#     pw = int(input("비밀번호를 입력하세요: "))
#     if pw ==passwd:
#      print("로그인 되었습니다.")

ID = "python"
PW = "asdf"

user_id = input("user_id: ")
if ID == user_id:
    user_pw = input("user_pw: ")
    if PW == user_pw:
        print("로그인 성공")
    else:
        print("비번이 틀렸습니다.")
else:
    print("그런 아이디는 존재하지 않습니다.")
    


