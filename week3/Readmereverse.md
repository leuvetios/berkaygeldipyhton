str = input("Bir cümle ya da kelime giriniz :")
## Kullanıcıdan bir cümle veya kelime aldık
index = len(str)
#bunu bir değişkene len uzunluğuna göre hesapladık
new_str = []
##boş bir liste açtık
while index :
###Döngümüzü index(len değişkenine göre ayarladık)
#dönügünün içinde index 1 azalttık

    index -= 1
## Listemizin içine STR aldığımız kelime veya cümleyi indexleri tersten atarak kelime harf harf yazdırdık
    new_str.append(str[index])
##liste değil de normal yanyana yazılması için kodumuzu yazdık
new2_str= ''.join(new_str)
##Bunu yeni değişkenimizi buraya yazdırdık
print(new2_str)
