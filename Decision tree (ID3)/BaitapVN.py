import pandas as pd
import math
import matplotlib.pyplot as plt

# 1. TẠO DỮ LIỆU
data = {
    "age": [
        "<=30", "<=30", "31...40", ">40", ">40",
        ">40", "31...40", "<=30", "<=30", ">40",
        "<=30", "31...40", "31...40", ">40"
    ],

    "income": [
        "high", "high", "high", "medium", "low",
        "low", "low", "medium", "low", "medium",
        "medium", "medium", "high", "medium"
    ],

    "student": [
        "no", "no", "no", "no", "yes",
        "yes", "yes", "no", "yes", "yes",
        "yes", "no", "yes", "no"
    ],

    "credit_rating": [
        "fair", "excellent", "fair", "fair", "fair",
        "excellent", "excellent", "fair", "fair", "fair",
        "excellent", "excellent", "fair", "excellent"
    ],

    "buys_computer": [
        "no", "no", "yes", "yes", "yes",
        "no", "yes", "no", "yes", "yes",
        "yes", "yes", "yes", "no"
    ]
}
df = pd.DataFrame(data)

# 2. TÍNH ENTROPY
def entropy(data):
    so_luong = data.value_counts()
    tong = len(data)
    H = 0
    for n in so_luong:
        p = n / tong
        H = H - p * math.log2(p)

    return H

# 3. TÍNH INFORMATION GAIN
def information_gain(df, attribute, target):

    H_truoc = entropy(df[target])
    H_sau = 0

    for value in df[attribute].unique():

        nhom = df[df[attribute] == value]

        H_nhom = entropy(nhom[target])

        trong_so = len(nhom) / len(df)

        H_sau = H_sau + trong_so * H_nhom
    gain = H_truoc - H_sau

    return gain

# 4. CHỌN THUỘC TÍNH TỐT NHẤT
def chon_thuoc_tinh(df, attributes, target):

    gain_lon_nhat = -1
    thuoc_tinh_tot_nhat = None

    for attribute in attributes:
        gain = information_gain(
            df,
            attribute,
            target
        )

        print(
            "Gain(", attribute, ") =",
            round(gain, 3)
        )

        if gain > gain_lon_nhat:

            gain_lon_nhat = gain
            thuoc_tinh_tot_nhat = attribute
    return thuoc_tinh_tot_nhat

# 5. THUẬT TOÁN ID3
def ID3(df, attributes, target):

    # Nếu tất cả mẫu cùng một lớp
    if len(df[target].unique()) == 1:

        return df[target].iloc[0]

    # Nếu không còn thuộc tính
    if len(attributes) == 0:

        return df[target].mode()[0]

    # Chọn thuộc tính tốt nhất
    best_attribute = chon_thuoc_tinh(
        df,
        attributes,
        target
    )
    print("=> Chọn:", best_attribute)

    # Tạo cây
    tree = {}

    tree[best_attribute] = {}

    # Các thuộc tính còn lại
    attributes_con_lai = []

    for attribute in attributes:

        if attribute != best_attribute:

            attributes_con_lai.append(attribute)

    # Tạo các nhánh
    for value in df[best_attribute].unique():

        nhom = df[
            df[best_attribute] == value
        ]
        if len(nhom) == 0:

            tree[best_attribute][value] = \
                df[target].mode()[0]
        else:
            tree[best_attribute][value] = ID3(
                nhom,
                attributes_con_lai,
                target
            )
    return tree

# 6. CHẠY ID3
attributes = [
    "age",
    "income",
    "student",
    "credit_rating"
]
print("================================")
print("        ENTROPY BAN ĐẦU")
print("================================")
H = entropy(df["buys_computer"])

print("Entropy =", round(H, 3))
print("\n================================")
print("      INFORMATION GAIN")
print("================================")

for attribute in attributes:
    gain = information_gain(
        df,
        attribute,
        "buys_computer"
    )
    print(
        attribute,
        "=",
        round(gain, 3)
    )

print("\n================================")
print("          XÂY CÂY ID3")
print("================================")
cay = ID3(
    df,
    attributes,
    "buys_computer"
)


# 7. VẼ CÂY
fig, ax = plt.subplots(figsize=(14, 8))

ax.axis("off")

def ve_cay(
    tree,
    x,
    y,
    dx,
    parent=None,
    text=""
):
    # Nếu là lá YES / NO
    if not isinstance(tree, dict):
        ax.text(
            x,
            y,
            tree.upper(),
            fontsize=13,
            ha="center",
            va="center",
            bbox=dict(
                boxstyle="round",
                facecolor="lightgreen"
            )
        )
        if parent is not None:

            ax.plot(
                [parent[0], x],
                [parent[1], y],
                "k-"
            )
            ax.text(
                (parent[0] + x) / 2,
                (parent[1] + y) / 2,
                text,
                fontsize=11,
                ha="center"
            )
        return

    # Lấy tên thuộc tính
    attribute = list(tree.keys())[0]

    # Vẽ nút
    ax.text(
        x,
        y,
        attribute,
        fontsize=13,
        ha="center",
        va="center",
        bbox=dict(
            boxstyle="round",
            facecolor="lightblue"
        )
    )
    # Nối với nút cha
    if parent is not None:

        ax.plot(
            [parent[0], x],
            [parent[1], y],
            "k-"
        )

        ax.text(
            (parent[0] + x) / 2,
            (parent[1] + y) / 2,
            text,
            fontsize=11,
            ha="center"
        )

    # Lấy các nhánh
    branches = tree[attribute]

    so_nhanh = len(branches)

    khoang_cach = dx * 2

    start_x = x - (
        (so_nhanh - 1) * khoang_cach / 2
    )
    i = 0

    for value in branches:
        child_x = start_x + i * khoang_cach
        child_y = y - 2

        ve_cay(
            branches[value],
            child_x,
            child_y,
            dx / 2,
            (x, y),
            str(value)
        )
        i = i + 1

# Vẽ cây
ve_cay(
    cay,
    0,
    0,
    2
)

# Tiêu đề
plt.title(
    "Cây quyết định ID3",
    fontsize=18
)
plt.show()