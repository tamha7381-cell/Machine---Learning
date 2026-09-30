# Hàm số
def f(x):
    return x**2 - 4*x + 5

# Đạo hàm
def grad(x):
    return 2*x - 4

# Gradient Descent
def myGD(x0, eta, n):
    x = [x0]

    for it in range(n):
        x_new = x[-1] - eta * grad(x[-1])
        x.append(x_new)

    return x


# Thông số bài toán
x0 = 5
eta = 0.2
n = 4

# Chạy Gradient Descent
x = myGD(x0, eta, n)

# In kết quả
for i in range(len(x)):
    print("Bước", i)
    print("x =", x[i])
    print("f(x) =", f(x[i]))
    print("f'(x) =", grad(x[i]))
    print()