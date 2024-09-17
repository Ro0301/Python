
t=int(input("Nhập số giây:"))
giờ=(t//3600)%24
phút=(t%3600)//60
giây=(t%3600)%24
print(giờ,":",phút,":",giây)