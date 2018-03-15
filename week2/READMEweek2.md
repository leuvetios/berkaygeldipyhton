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



# Soru 2 

        # K ile D boş liste oluşturdum
        k = []
        d = []
        # a ve b adında (input alarak) kullanıcıdan başlangıç ve sonuç değerini istedik
        a = input ("Başlangıç : ")
        b = input ( "Son : ")
        # c değişkeni ile kullanıcıdan bir cümle veya kelime aldık , A başlangıç ve B son değerine göre harfleri getiricek
        c = input ( "Cümlenizi veya Kelimenizi Giriniz :")
        #aldığımız kelime veya cümleyi burdan d[] listesine harf harf atıyoruz
        d += c
        #açtığımız k değişkenine atıyoruz
        k = d
        #K listesinde a(1) ve b(4) harflerini getirir Kullanıcı pamir yazınca ( PR ) getirir .
        k[int(a):int(b)] = []
        #Yeni bir değişken açıp ['P','R'] gözükmesin diye " PR " gözüksün diye join komutu ile listeyi kaldırıp boşlukları kaldırdım.
        L = "".join(k)
        #L yi yazdırdım
        print(L)

        ### Not: benim yazdığım kod'da index'e göre olduğu için P 0 harfinden başlıyor hocam o yüzden 2:4 1:4 o sonucu getirebilirsiniz..
        
        
# Soru 3 

       #Bir liste oluşturmak için boş bir liste açtık
        a = []
        s = input("Bir cümle yada kelime giriniz : ")
        #Kullanıcıdan bir cümle yada kelime giriniz
        a += s
        #inputtan aldığımız a değişkenine harf olarak atar , tek tek attık 

        #yeni bir değişken açtık ii(sayac olarak kullandık ' n kadar , ii sayacını enumarate(a)//a değişkinene atınan cümledeki harfleri index
        ## numaraları gibi atadık eğer ii a[:n] a harfi atadığımız n karakterine eşitse newlist listemize almıcak eğer değilse alıp yazdırıcak
        newList =[ii for n , ii in enumerate(a) if ii not in a[:n]]

        # bir değişken açıp join komutuyla aradaki newlist atılan harfleri birleştirdik
        d= "".join(newList)
        # ekrana yazdırdık
        print(d)
        
        
        
# Soru 4 

        #Bir boş liste açıyorum
        a = []
        #Kelime istiyorum input ile 
        s = input("Polidromu denediğiniz kelimeyi veya Cümleyi giriniz : ")
        # inputtan aldığım cümle veya kelimeyi a listesine atıyorum
        s = a

        #kolaylık olması bakımısından my_str diye bir değişkene atıyorum 
        my_str = s
        #rev_str değişkenine atıyoruz reserved kodu ile tersini alıyoruz
        rev_str = reversed(my_str)
        #if ile değişkeni kontrol ediyoruz eğer eşitse polidromdur
        if list(my_str) == list(rev_str):
        print("polidromdur")
        #değilse polidrom değildir
        else:
        print("polidrom değildir")

