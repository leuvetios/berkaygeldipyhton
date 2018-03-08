# pyhton 1. Teknik

        import random
        s = 0
        arr = [None] * 100
        for i in range(1, 100):

        arr[i] = i


        arr[0] = random.randint(1, 99)
        print(arr)
        random.shuffle(arr)
         #toplam diye değişken atadık
        toplam = 0
         #Döngü açıp i yi tekrar arr ile döngüye soktuk
        for i in arr :
                toplam = toplam + i
        #toplam değişkenine i yi attık
                 sayi = toplam - 4950
        print ("random sayi :",sayi)
        #toplam değişkeninden - 4950 (99 sayının toplamıyla çıkardık)

# soru 1 2.teknik
       import random
        s = 0
        arr = [None] * 100
        for i in range(1, 100):

            arr[i] = i
            arr2 = i


            arr[0] = random.randint(1, 99)
            print(arr)

            random.shuffle(arr)


           #Bir değişken açtım x ile başlıcak n sayıya kadar  , x sayısı (enumarate " listedeki her öğeye numara verir " ) arr listesinin her öğesine
           ## numara verdim eğer x inn arr [arr:n] en son yüklenen kullanıcısına gelirse randomu bulucak.Biraz kolaylığa kaçtım gibi :) 
           ### ama aklıma  bu geldi.. 

           randoms = [x for n, x in enumerate(arr) if x in arr[:n]]
           print ("Random Sayımız  : ", randoms)

