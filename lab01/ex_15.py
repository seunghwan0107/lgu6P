# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))
# x = float(input("x: "))

# y1 = a * x + b
# print(y1)

# y2 = a * x**2 + b * x + c
# print(y2)
# /////////////////////////////////////////////////////

# x = float(input("x: "))
# mu = float(input("mu: "))
# sigma = float(input("sigma: "))

# # 1/sigma(2.506)*2.718*(-(x-mu)/2(sigma*sigma))

# a = 1/sigma*2.506
# b = -(x-mu)(x-mu)/2*sigma(sigma)
# e = 2.718

# print(f"{a}*{e}*{b}")
# ////////////////////////////////////////////

x = float(input("x: "))
mu = float(input("mu: "))
sigma = float(input("sigma: "))

e = 2.718
sqrt_2pi = 2.506
var = sigma*sigma
nomal = (1 / (sigma*sqrt_2pi))* e **((-(x-mu)**2)/(2*var))
print(nomal)
