while True :
    n = int(input("Nhập một số để kiểm tra snt :"))
    dem = 0

    for i in range(2,n+1):
        if n % i == 0:
            dem += 0

    if dem == 2 :
        print(f"Số {n} nguyên tố ")
    else :
        print(f"Số {n} không phải số nt")

    hoi = input("Bạn muốn kiểm tra nữa hay không (y or n):")
    if hoi == 'n' :
        break

print("Bye!")

