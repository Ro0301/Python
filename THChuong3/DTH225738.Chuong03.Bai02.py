
month = int(input("Nhập vào một tháng (1-12):"))

while month > 12 or month < 0 :
    print(" Vui lòng nhập lại một tháng :",end="")
    month = int(input())

if month in (1,3,5,7,8,10,12):
    print(f"Tháng {month} có 31 ngày")
elif month in (4,6,8,11):
    print(f" Tháng {month} có 30 ngày")
elif month == 2:
    year = int(input("Nhập vào một năm để kiểm tra năm nhuận :"))
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"Tháng 2 năm {year} có 29 ngày")
    else :
        print(f"Tháng 2 năm {year} có 28 ngày")
