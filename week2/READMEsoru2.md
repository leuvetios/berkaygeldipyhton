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
