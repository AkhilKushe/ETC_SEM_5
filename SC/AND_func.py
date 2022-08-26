

x1, x2 = map(int, input("Enter x1 and x2 (space seperated) : ").split())

w1 = 1
w2 = 1
b = -1
net = x1*w1 + x2*w2 + b


print("Output = ", 1 if net >= 0 else 0)

input("Press ener to exit")


