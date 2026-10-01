import matplotlib.pyplot as plt

# 1. TẠO KHUNG HÌNH
fig, ax = plt.subplots(figsize=(12, 8))

# Cho phép co giãn cửa sổ
fig.canvas.manager.set_window_title("Cây quyết định ID3")

# 2. TẠO HÀM VẼ Ô
def ve_o(x, y, text, mau):
    ax.text(
        x, y, text,
        ha="center",
        va="center",
        fontsize=13,
        fontweight="bold",
        bbox=dict(
            boxstyle="round,pad=0.5",
            facecolor=mau,
            edgecolor="black",
            linewidth=1.5
        )
    )

# 3. VẼ CÁC NÚT
# Nút gốc
ve_o(0.5, 0.9, "age", "lightblue")

# Tầng 2
ve_o(0.25, 0.65, "student", "lightblue")
ve_o(0.5, 0.65, "YES", "lightgreen")
ve_o(0.75, 0.65, "credit_rating", "lightblue")

# Tầng cuối
ve_o(0.15, 0.35, "NO", "lightcoral")
ve_o(0.35, 0.35, "YES", "lightgreen")

ve_o(0.65, 0.35, "YES", "lightgreen")
ve_o(0.85, 0.35, "NO", "lightcoral")

# 4. VẼ MŨI TÊN
def mui_ten(x1, y1, x2, y2):
    ax.annotate(
        "",
        xy=(x2, y2),
        xytext=(x1, y1),
        arrowprops=dict(
            arrowstyle="->",
            linewidth=1.5,
            color="black"
        )
    )

# age → các nhánh
mui_ten(0.5, 0.87, 0.25, 0.69)
mui_ten(0.5, 0.87, 0.5, 0.69)
mui_ten(0.5, 0.87, 0.75, 0.69)

# student → kết quả
mui_ten(0.25, 0.62, 0.15, 0.39)
mui_ten(0.25, 0.62, 0.35, 0.39)

# credit_rating → kết quả
mui_ten(0.75, 0.62, 0.65, 0.39)
mui_ten(0.75, 0.62, 0.85, 0.39)


# 5. GHI GIÁ TRỊ TRÊN NHÁNH
ax.text(0.35, 0.80, "<=30", fontsize=11)
ax.text(0.52, 0.80, "31...40", fontsize=11)
ax.text(0.66, 0.80, ">40", fontsize=11)

ax.text(0.18, 0.51, "no", fontsize=11)
ax.text(0.31, 0.51, "yes", fontsize=11)

ax.text(0.68, 0.51, "fair", fontsize=11)
ax.text(0.80, 0.51, "excellent", fontsize=11)

# 6. TIÊU ĐỀ
ax.set_title(
    "CÂY QUYẾT ĐỊNH ID3",
    fontsize=20,
    fontweight="bold",
    pad=20
)

# 7. CHỈNH KHUNG
ax.set_xlim(0, 1)
ax.set_ylim(0.2, 1)

ax.axis("off")

# 8. HIỂN THỊ
plt.tight_layout()
plt.show()


