def topla(sayi,kacar=1) :
    toplam = 0
    i = 0
    while sayi > i :
        toplam += i
        i += kacar
    print("Toplam:", toplam)

topla(10,3)
