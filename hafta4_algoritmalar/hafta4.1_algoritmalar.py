
#1-kullanıcının girdiği 2 sayı arasındaki sayıların toplamını bulan Sorgu
#For ile
print("4. Hafta Ödevi: 1\n2 sayı arasındaki sayıların toplamını bulan program")
say1 = int(input("Birinci sayıyı giriniz: "))
say2 = int(input("İkinci sayıyı giriniz: "))
toplam = 0
if say1 < say2:
    for i in range((say1+1),say2,1):
        toplam+=i
elif say2 < say1:
    for i in range((say2+1),say1,1):
        toplam+=i
print("Girdiğiniz iki sayı arasındaki tamsayıların toplamı: {}".format(toplam))