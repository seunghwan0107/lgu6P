
# def dummy():
#     print("i am dummy function.")
#     print("end function")

# print(dummy())

# def dummy2():
#     print('i am a dummy function2')
#     return 10

# print(dummy2())

# R = dummy2()

# print(R)
# # print(), range(), int()
# # float(), bool(), type()


# def add(a,b):
#     c= a+b
#     print(c)
#     return c

# c = add(1,2)
# print(c)

#############################################################

# x = 'global variable'

# def print_x():
#     print(x)
#     x = 'local variable'
#     print(x)

# print_x()
# print(x)

##########################################################
#기본 인자

def greet(name, greeting= "hello"):
    print(f"{greeting},{name}")

greet('홍길동','안녕')
greet('홍길동')
########################################################
#위치 인자

def op(x,z,y):
    return(x+y)*z

x = 2
y = 3
z = 4

print(op(x,y,z))