import pandas as pd
import math
# 1. TẠO DỮ LIỆU
data = {
    "Tuoi": [25, 40, 35, 27, 31, 36, 48, 26, 33, 29,
             38, 44, 42, 28, 30],

    "HonNhan": [
        "Độc thân", "Đã kết hôn", "Từng ly hôn",
        "Đã kết hôn", "Độc thân", "Đã kết hôn",
        "Độc thân", "Đã kết hôn", "Từng ly hôn",
        "Độc thân", "Đã kết hôn", "Độc thân",
        "Đã kết hôn", "Độc thân", "Đã kết hôn"
    ],

    "SoHuuBDS": [
        "Ở cùng bố mẹ", "Nhà sở hữu", "Nhà thuê",
        "Ở cùng bố mẹ", "Nhà thuê", "Nhà sở hữu",
        "Nhà thuê", "Nhà thuê", "Ở cùng bố mẹ",
        "Nhà thuê", "Nhà sở hữu", "Nhà sở hữu",
        "Nhà sở hữu", "Nhà thuê", "Ở cùng bố mẹ"
    ],

    "ThuNhap": [
        7000000, 18000000, 12000000, 9000000, 6000000,
        8000000, 7000000, 8000000, 5000000, 10000000,
        15000000, 14000000, 10000000, 7000000, 6000000
    ],

    "RuiRo": [
        0, 0, 1, 1, 1,
        1, 0, 1, 1, 0,
        0, 1, 0, 1, 1
    ]
}
df = pd.DataFrame(data)

# 2. RỜI RẠC HÓA DỮ LIỆU
def phan_loai_tuoi(x):
    if x <= 30:
        return "<=30"
    elif x <= 40:
        return "31-40"
    else:
        return ">40"

def phan_loai_thu_nhap(x):
    if x <= 8000000:
        return "<=8tr"
    elif x <= 12000000:
        return "8-12tr"
    else:
        return ">12tr"
df["Tuoi"] = df["Tuoi"].apply(phan_loai_tuoi)
df["ThuNhap"] = df["ThuNhap"].apply(phan_loai_thu_nhap)

# 3. TÍNH ENTROPY
def entropy(y):
    values = y.value_counts()
    total = len(y)
    ent = 0

    for count in values:
        p = count / total
        ent -= p * math.log2(p)
    return ent

# 4. TÍNH INFORMATION GAIN
def information_gain(df, attribute, target):
    total_entropy = entropy(df[target])
    weighted_entropy = 0

    for value in df[attribute].unique():
        subset = df[df[attribute] == value]
        weight = len(subset) / len(df)
        weighted_entropy += weight * entropy(subset[target])
    return total_entropy - weighted_entropy

# 5. CHỌN THUỘC TÍNH TỐT NHẤT
def best_attribute(df, attributes, target):
    gains = {}
    for attribute in attributes:
        gains[attribute] = information_gain(
            df, attribute, target
        )
    best = max(gains, key=gains.get)
    print("\nInformation Gain:")
    for attr, value in gains.items():
        print(f"{attr}: {value:.6f}")
    print("=> Thuộc tính được chọn:", best)
    return best


# 6. THUẬT TOÁN ID3
def ID3(df, attributes, target):
    # Nếu tất cả mẫu cùng một lớp
    if len(df[target].unique()) == 1:
        return int(df[target].iloc[0])

    # Nếu không còn thuộc tính
    if len(attributes) == 0:
        return int(df[target].mode()[0])

    # Chọn thuộc tính có Gain lớn nhất
    best = best_attribute(
        df, attributes, target
    )
    tree = {best: {}}

    # Xây cây cho từng giá trị
    for value in df[best].unique():
        subset = df[df[best] == value]
        remaining_attributes = [
            attr for attr in attributes
            if attr != best
        ]
        tree[best][value] = ID3(
            subset,
            remaining_attributes,
            target
        )
    return tree

# 7. XÂY DỰNG CÂY
attributes = [
    "Tuoi",
    "HonNhan",
    "SoHuuBDS",
    "ThuNhap"
]
tree = ID3(
    df,
    attributes,
    "RuiRo"
)


# 8. IN CÂY 
def print_tree(tree, space=""):
    # Nếu là nút lá
    if not isinstance(tree, dict):
        print(space + "→ Rủi ro =", tree)
        return

    attribute = next(iter(tree))

    for value, subtree in tree[attribute].items():

        print(
            space +
            "[" + attribute + " = " + str(value) + "]"
        )

        if isinstance(subtree, dict):
            print_tree(
                subtree,
                space + "    "
            )
        else:
            print(
                space +
                "    → Rủi ro = " +
                str(subtree)
            )
print("\n================================")
print("CÂY QUYẾT ĐỊNH XÂY DỰNG TỪ ID3")
print("================================")
print_tree(tree)