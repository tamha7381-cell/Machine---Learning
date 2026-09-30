import numpy as np

w = np.array([-2, 1, 0])
x = np.array([2, 3, 1])
y = 1

# Tính w^T x
wx = np.dot(w, x)

print("w^T x =", wx)

# Dự đoán
y_pred = 1 if wx >= 0 else -1

print("Nhãn dự đoán =", y_pred)

# Kiểm tra phân lớp sai
if y_pred != y:

    print("Mẫu bị phân lớp sai")

    # Learning rate
    eta = 1

    # Cập nhật Perceptron
    w = w + eta * y * x

    print("w sau cập nhật =", w)

    # Tính lại w^T x
    wx_new = np.dot(w, x)

    print("w^T x sau cập nhật =", wx_new)

    # Dự đoán lại
    y_pred_new = 1 if wx_new >= 0 else -1

    print("Nhãn dự đoán mới =", y_pred_new)

else:
    print("Mẫu được phân lớp đúng")