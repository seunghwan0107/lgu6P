
# def get_number_generator(n):
#     for i in range(n):
#         print("befaore yield")
#         yield i
#         print("after yield")

# number = get_number_generator(3)
# print(next(number,'end'))
# print()
# print(next(number,'end'))
# print()
# print(next(number,'end'))
# print()

# # 리스트로 감싸면 한번에 다 소진한다

# for i in g:
#     print(i)

#무한 제너레이터

def generator():
    x = 1
    while True:
        yield x
        x += 1

g = generator()
print(next(g))