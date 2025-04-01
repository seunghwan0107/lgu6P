# h = float(input("키(M): "))
# w = float(input("몸무게(Kg): "))

# print("BMI는: ",w/h**2)

# # h*h , h**2 같음

h = float(input("키(M): "))
w = float(input("몸무게(kg): "))

bmi = round(w/h**2,3)
print("BMI: ",bmi)