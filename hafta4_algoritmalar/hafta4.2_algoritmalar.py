
#2-Klavyeden ardı ardına sayı girişi isteyen ve bu sayı 10 ile 15 arasında
#olmadığı sürece bu işleme devam eden programı yazınız.
print("4. Hafta Ödevi: 2: \n 10-15 arasi sayi girildiğinde programdan çıkılacaktır.")
while True:
    try:
        sayi = int(input("Tamsayı giriniz: "))
    except:
        print("Tamsayı giriniz.")
        sayi = 0
    if sayi >= 10 and sayi <= 15:
         print("Programdan çıkılıyor.")
         break
    