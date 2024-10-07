x = int(input("Nhập gia trị x :"))
n = int(input("Nhập gia trị n :"))

s = 0

for i in range(1,n+1):
    tu = x**i
    mau = 1
    for j in range(1,i+1):
        mau *=j
    s += (tu/mau)

print(f"s({x},{n})={s}")

