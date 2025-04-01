# #ex_str.py

# s = "Hello Python"
# print(s)

# s = 'Hello Python'
# print(s)

# s = "Hello \"Easy\" Python"
# print(s)

# s='Hello "Easy" Python'
# print(s)

# s = "Hello \nEasy Python"
# print(s)

# print(type(s))

# s= """Hello,
#        "EaSY"Python
# """
# print(s)

# ########################################
# # F-string
# ########################################

# a = 10
# b = 20
# c = a*b
# # print('c:',c,'success')
# # print(f"c: {c} Success")
# print(f"{a}x{b}={c:.1f}")

# # d = 5
# # e = 20
# # f = d*e
# # print('f:',f,'fail')  
# d=5.2
# e=21.232
# f=d*e
# print(f"{d}x{e}={f:.1f}")

# a = "Hello"
# print(f"{a:ㅁ^20}")

s = "python,python"
print(type(s))

#count()
print(s.count('python')) 
# 몇번 나왔는지

#find()
print(s.find('t'))
print(s.find('x'))
# T의 인덱스값 찾아줌
# 없는거면 -1나옴

#replace()
print(s.replace('python','PYTHON'))
print(s) #원래값이 영구적으로 바뀌는건 아님
#바꿔주세여

#split()
print(s.split(',')) #기본값은 ' '스페이스
# ,로 쪼개라 리스트로 받음

#join()
L = ['python','java','c++']
print(','.join(L))
# L = join(',')이거안댐
#하나의 리스트르 붙이고 싶을때

#strip()
s = " python \n\t "
print(s.strip())
print(f"|{s.strip()}|")
#앞뒤 공백없앴네 벗기는거

s[1:-1]
s = "@<python>!"
print(f"|{s.strip('<>@!')}|")

#isdigit
# (), isalpha(), isalum()
s = "123a"
print(s.isdigit())
#숫자냐 아니냐
print(s.isalpha())
#알파벳이냐 아니냐
print(s.isalnum())
#알파벳하고 숫자

#upper(), lower()
s = 'PyTHon'
print(s.upper()) # 싹다 대문자
print(s.lower()) # 싹다 소문자