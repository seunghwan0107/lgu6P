# r = float(input("원의 반지름을 입력하세요: "))
# p = 3.14
# a = p*(r**2)
# b = 2*p*r
# c = 2*r

# print(f"반지름이 {r:.1f}인 원의 면적은 {a}입니다.")
# print(f"이 원의 둘레는 {b}입니다.")
# print(f"이 원의 지름은 {c}입니다.")

pi = 3.14

radius = float(input("원의 반지름을 입력하세요: "))

area = pi*radius*radius
circum = 2 * pi * radius
d = radius * 2
area = round(area,1)

print(f"면적 {area}, 둘래{circum}, 지름{d}")