year = int(input("Bạn hãy nhập vào một năm để kiểm tra :"))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(f"Năm {year} là năm nhuần ")
else :
    print(f"Năm {year} không phải năm nhuần")