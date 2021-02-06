print("HESAP MAKİNESİ")
print("""
1 = Toplama
2 = Çıkarma
3 = Çarpma
4 = Bölme
""")
islem = input("İşlem Seçiniz: ")

if islem == "1":
    top1 = int(input("Birinci Sayı: "))
    top2 = int(input("İkinci Sayı: "))
    tops = topl + top2
    print("Sonuç = ",tops)
elif islem == "2":
    cik1 = int(input("Birinci Sayı: ")) 
    cik2 = int(input("İkinci Sayı: "))
    ciks = cik1 - cik2
    print("Sonuş = ",ciks)
elif islem == "3":
    carl1 = int(input("Birinci Sayı: "))
    carl2 = int(input("İkinci Sayı: "))
    carls = car1 * car2
    print("Sonuç = ",cars)
elif islem == "4":
    bol1 = int(input("Birinci Sayı: "))
    bol2 = int(input("İkinci Sayı: "))
    bols = bol1 / bol2 
    print("Sonuç = ",bols)
    banner="""
    ##########################
#Makraz HesapMakinesi   V1.0     #
#Code by Makraz      #
##########################