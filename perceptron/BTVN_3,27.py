import numpy as np

w = np.array([1, 2, -10])
x = np.array([3, 4, 1])

# Tính w^T x
wx = np.dot(w, x)

print("w^T x =", wx)

# Dự đoán nhãn
y_pred = 1 if wx >= 0 else -1

print("Nhãn dự đoán =", y_pred)

# Nhãn thực tế
y = -1

if y_pred != y:
    print("Điểm dữ liệu bị phân lớp sai")
else:
    print("Điểm dữ liệu được phân lớp đúng")