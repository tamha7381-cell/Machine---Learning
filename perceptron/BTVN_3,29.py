import numpy as np


class Perceptron:

    def __init__(self, eta=0.1, epochs=10):
        self.eta = eta
        self.epochs = epochs
        self.w = None

    # Hàm huấn luyện
    def fit(self, X, y):

        # Khởi tạo trọng số
        self.w = np.zeros(X.shape[1])

        # Huấn luyện
        for epoch in range(self.epochs):

            for i in range(len(X)):

                # Tính w^T x
                z = np.dot(self.w, X[i])

                # Dự đoán
                y_pred = 1 if z >= 0 else -1

                # Nếu sai thì cập nhật
                if y_pred != y[i]:
                    self.w = self.w + self.eta * y[i] * X[i]

        return self

    # Hàm dự đoán
    def predict(self, X):

        result = []

        for i in range(len(X)):

            # Tính w^T x
            z = np.dot(self.w, X[i])

            # Dự đoán nhãn
            y_pred = 1 if z >= 0 else -1

            result.append(y_pred)

        return np.array(result)


# Dữ liệu mẫu
X = np.array([
    [2, 3],
    [3, 4],
    [-2, -3],
    [-3, -4]
])

y = np.array([1, 1, -1, -1])


# Tạo mô hình
model = Perceptron(
    eta=0.1,
    epochs=10
)

# Huấn luyện
model.fit(X, y)

# Dự đoán
y_pred = model.predict(X)

print("Trọng số:", model.w)
print("Nhãn thực tế:", y)
print("Nhãn dự đoán:", y_pred)