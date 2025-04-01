S = "python"
print(S[0])

# TypeError
# i = 123
# print(i[0])

for s in S:
    print(s)

# TypeError 불변이라 못바꿈
# S[0] = 'p'

########################################################

#Tuple = 순서쌍
#          0        1          2  
zoo = ('python','elephant','penguin')
print(zoo)
print(zoo[0])

#IndexError: tuple index out of range
# print(zoo[3])

# #TypeError: tuple indices must be integers or slices, not str
# print(zoo['c'])

# TypeError: 'tuple' object does not support item assignment
# zoo[0] = 'lion'

sigloton = ('lion',)
print(type(sigloton))


#패킹 언패킹

numbers = 1,2,3
print(numbers)

i1 = numbers[0]
i2 = numbers[1]
i3 = numbers[2]

i1,i2,i3,i4 = numbers  #i4는 오류 위에 i1 2 3말고 아래처럼 해도됨

############################################################