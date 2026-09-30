# Phân lớp nhị phân bằng Perceptron

import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Đọc dữ liệu
data = load_breast_cancer()

X = data.data
y = data.target

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Chuẩn hóa dữ liệu
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Xây dựng lớp Perceptron
class Perceptron:

    def __init__(self, eta=0.01, n_iter=100):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):

        self.w = np.zeros(X.shape[1])
        self.b = 0

        y_new = np.where(y == 0, -1, 1)

        for _ in range(self.n_iter):

            for xi, yi in zip(X, y_new):

                z = np.dot(xi, self.w) + self.b

                y_pred = 1 if z >= 0 else -1

                if y_pred != yi:
                    self.w += self.eta * yi * xi
                    self.b += self.eta * yi
        return self

    def predict(self, X):
        z = np.dot(X, self.w) + self.b
        return np.where(z >= 0, 1, 0)

# Huấn luyện mô hình
model = Perceptron(
    eta=0.01,
    n_iter=100
)

model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá mô hình
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1-score :", f1)