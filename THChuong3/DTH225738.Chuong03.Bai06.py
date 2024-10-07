n = int(input("Nhập vào một số có hai chữ số:"))

c = n//10
dv = n%10

if c == 0 :
    c = ''
if c == 1 :
    c = 'Mười'
if c == 2 :
    c = 'Hai mươi'    
if c == 3 :
    c = 'Ba mươi'
if c == 4 :
    c = 'Bốn mươi'
if c == 5 :
    c = 'Năm mươi'
if c == 6 :
    c = 'Sau mươi'
if c == 7 :
    c = 'Bay mươi'
if c == 8 :
    c = 'Tám mươi'
if c == 9 :
    c = 'Chín mươi'

if dv == 0:
    dv = ""    
if dv == 1 :
    dv = 'một'
if dv == 2 :
    dv = 'hai'
if dv == 3 :
    dv = 'ba'
if dv == 4 :
    dv = 'bốn'
if dv == 5 :
    if n > 10:
        dv = 'lăm'
    else :
        dv = 'năm'   
if dv == 6 :
    dv = 'sáu'
if dv == 7 :
    dv = 'bảy'
if dv == 8 :
    dv = 'tám'
if dv == 9 :
    dv = 'chín'
    

print(f"{n}=>{c} {dv}")     