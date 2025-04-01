# a = -3

# if a > 0:
#     print("positive")
# elif a < 0:
#     print("negative")
# else :
#     print("zero")

# h = float(input("키(M): "))
# w = float(input("몸무게(kg): "))

# bmi = w/h**2

# if bmi < 18.5:
#     print("저체중")
# elif bmi >=25.00:
#     print("비만")
# elif 18.5 <= bmi <23:
#     print("정상")
# else :
#     print("과체중")


# height = float(input("키(M): "))
# weight = float(input("몸무게(kg): "))

# bmi = round(weight / height**2,3)

# if bmi < 18.5:
#     print("저체중")
# elif 18.5 <= bmi and bmi < 23:
#     print("정상")
# elif 23 <= bmi and bmi < 25:
#     print("과체중")
# else :
#     print("비만")

h = float(input("키(M): "))
w = float(input("몸무게(kg): "))

bmi = w/h**2

if bmi >= 25:
    print("비만")
elif 23 <= bmi:
    print("과체중")
elif 18.5 <= bmi: 
    print("정상")
else :
    print("저체중")


