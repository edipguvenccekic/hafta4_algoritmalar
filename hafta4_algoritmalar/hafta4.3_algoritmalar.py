
#3-Kullanıcının istediği kadar girdiği sayıların aritmetik ortalamasını,
#geometrik ortalamasını, en büyüğünü, en küçüğünü bulan programı
#yazınız.
print("Kullanıcı tarafından girilen değerlerin \nen büyüğünü, en küçüğünü, aritmetik ve \ngeometrik ortalamasını hesaplayan program.")
min_bul = 0
max_bul = 0
toplam = 0
carpim = 1
sayi = 0
geometrik = 0
aritmetik = 0
while True:
    try:
        sayi_gir = int(input("Sayı giriniz: "))
    except:
        print("Lutfen tamsayı giriniz: ")
        sayi_gir = 0
        continue
    if sayi_gir < min_bul or min_bul == 0:
        min_bul = sayi_gir
    if sayi_gir > max_bul or max_bul == 0:
        max_bul = sayi_gir
    toplam = toplam + sayi_gir
    carpim = carpim * sayi_gir
    sayi = sayi + 1
    aritmetik = toplam / sayi
    geometrik = carpim**(1/sayi)
    devam = input("\t\tDikkat: Sayi girişini durdurmak için q'ya basınız.")
    if devam == "q":
        break
print("Girilen değerlerin\nEn küçüğü\t\t: {}\nEn büyüğü\t\t: {}\nAritmetik ortalaması\t: {}\nGeometrik ortalaması\t: {}".format(min_bul, max_bul, aritmetik, geometrik))