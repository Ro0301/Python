Ngày = int(input(" Nhập ngày:"))
while True:
    if Ngày == 31:
        Tháng = int(input(" Nhập tháng(1,3,5,7,8,10):"))
        if  Tháng not in  (1,3,5,7,8,10):
            Tháng = int(input(" Nhập tháng(1,3,5,7,8,10):"))
        else:
            break
    else:
        Tháng = int(input(" Nhập tháng:"))

Năm = int(input (" Nhập năm :"))

if Ngày == 31 :
    if Tháng in (1,3,5,7,8,10):
        Ngày = 1
        Tháng += 1
    elif Tháng == 12 :
        Ngày = 1
        Tháng = 1
        Năm += 1
        
elif Ngày == 30 and Tháng in (4,6,9,11) :
    Ngày = 1
    Tháng += 1
    
elif Tháng == 2 :
    if Ngày == 29 and ((Năm % 4 == 0 and Năm % 100 != 0) or Năm % 400 == 0): 
        Ngày = 1
        Tháng += 1
    elif Ngày == 28 :
        if (Năm % 4 == 0 and Năm % 100 != 0) or Năm % 400 == 0:   
            Ngày += 1
        else :
            Ngày = 1
            Tháng += 1
else :
    Ngày += 1

print(f"Ngaày kế sau ngày vừa nhập là : {Ngày}/{Tháng}/{Năm}")                 
       