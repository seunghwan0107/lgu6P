operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else "오류: 0으로 나눌 수 없습니다"
}
x = float(input("첫 번째 숫자를 입력하세요: "))
y = float(input("두 번째 숫자를 입력하세요: "))
z = input("연산자를 입력하세요(+,-,*,/): ")

# if z in operations:
#     re = operations[z](x,y)
#     print(f"{x} {z} {y} = {int(re)}")

# else:
#     print("오류: 0으로 나눌 수 없습니다.")
if z in operations.keys():
     re = operations[z](x,y)
     print(f"{x} {z} {y} = {re}")
else:
     print("올바른 연산자가 아닙니다.")
