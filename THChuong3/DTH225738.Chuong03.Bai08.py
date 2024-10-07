a = int(input("Nhập số nguyên thứ nhất :"))
b = int(input("Nhập số nguyên thứ hai :"))

pt = input("Nhập phép tính :")

while  not (pt == '+' or pt == '-' or pt == '*' or pt == '/'):
    pt = input("Vui lòng nhập lại phép tính :")

if pt == '+':
    kp = a + b
    
if pt == '-':
    kp = a - b
    
if pt == '*':
    kp = a * b
    
if pt == '/':
    kp = a / b

print("Kết quả của phép tính = ",kp)    
    