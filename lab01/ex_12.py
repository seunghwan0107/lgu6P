# name = str(input("너의 이름: "))
# k = int(input("국어 점수: "))
# e = int(input("영어 점수: "))
# m = int(input("수학 점수: "))
# s = int(input("과학 점수: "))

# a = k+e+m+s
# b = float
# b = (k+e+m+s)/4

# print(name,"의 총점은",a,"이고 평균은",b,"입니다.")

name = input("너의 이름")
kor = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
mat = int(input("수학 점수: "))
sci = int(input("과학 점수: "))

total = kor+eng+mat+sci
mean = total/4
print(f"{name}의 총점은 {total}이고 평균은 {mean}입니다. ")