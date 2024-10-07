x = int(input("Nhập giá trị x :"))
n = int(input("Nhập vào giá trị n :"))

s = 0

for i in range(1,n+1):
    Tu = x**(i*2+1)
    Mau = 1
    for j in range(1,i+1):
        Mau=Mau*(j+j)*(2*j+1)
    s = s+(Tu/Mau)
print(f"s({x},{n})={s}")
