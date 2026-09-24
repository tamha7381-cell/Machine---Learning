# Hàm grad-tính đạo hàm của hàm f(x)
def grad(x):
    return 2*x
    # Vì f(x) = x² - 2
    # nên f'(x) = 2x
    # Hàm này trả về giá trị đạo hàm tại x

# Hàm cost-tính giá trị của hàm f(x)
def cost(x):
    return x**2 - 2
    # x**2 nghĩa là x²
    # Đây chính là hàm cần tìm giá trị cực tiểu:
    # f(x) = x² - 2

# Hàm myGD1 thực hiện thuật toán Gradient Descent
def myGD1(x0, eta):
    # x0: giá trị x ban đầu
    # eta: learning rate (tốc độ học)

    x = [x0]
    # Tạo một danh sách để lưu các giá trị x qua từng lần lặp
    # Ban đầu danh sách chứa x0
    # Ví dụ x0 = 2 thì: x = [2]

    for it in range(100):
        # Thực hiện tối đa 100 lần lặp
        # it là số thứ tự của lần lặp
        # it sẽ lần lượt nhận: 0, 1, 2, ..., 99

        x_new = x[-1] - eta*grad(x[-1])
        # CÔNG THỨC QUAN TRỌNG NHẤT của Gradient Descent:
        # x_(t+1) = x_t - eta*f'(x_t)
        # x[-1] là giá trị x mới nhất hiện tại
        # grad(x[-1]) là đạo hàm tại giá trị x hiện tại
        # eta là learning rate
        # Với bài này: grad(x) = 2x nên: x_new = x[-1] - eta*(2*x[-1])

        if abs(grad(x_new)) < 1e-3:
            # Kiểm tra xem đạo hàm đã đủ gần 0 chưa
            # abs() lấy giá trị tuyệt đối
            # 1e-3 = 0.001
            # Nếu |f'(x_new)| < 0.001
            # thì coi như đã gần điểm cực trị → dừng thuật toán

            break
            # Thoát khỏi vòng lặp for ngay lập tức

        x.append(x_new)
        # Nếu chưa đạt điều kiện dừng
        # thì thêm giá trị x mới vào danh sách x

    return (x, it)
    # Trả về 2 thứ:
    # 1. x: danh sách các giá trị x qua từng lần lặp
    # 2. it: số thứ tự của lần lặp cuối cùng

# Gọi hàm Gradient Descent
x, it = myGD1(2, 0.1)
# x0 = 2: bắt đầu từ x = 2
# eta = 0.1: learning rate = 0.1
# Sau khi chạy: x sẽ chứa các giá trị x trong quá trình Gradient Descent
# it là số lần lặp

print("Các giá trị x:", x)
# In ra toàn bộ các giá trị x để xem x tiến dần về đâu

print("Số lần lặp:", it)
# In ra số thứ tự lần lặp cuối cùng

print("x tối ưu:", x[-1])
# x[-1] lấy giá trị cuối cùng trong danh sách x, đây là giá trị x gần điểm cực tiểu nhất

print("Giá trị cực tiểu:", cost(x[-1]))
# Đưa x tối ưu vào hàm f(x) : f(x) = x² - 2 để tính giá trị cực tiểu của hàm