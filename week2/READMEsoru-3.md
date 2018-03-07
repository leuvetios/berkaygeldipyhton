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
