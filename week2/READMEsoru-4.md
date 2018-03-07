#Bir boş liste açıyorum
a = []
#Kelime istiyorum input ile 
s = input("Polidromu denediğiniz kelimeyi veya Cümleyi giriniz : ")
# inputtan aldığım cümle veya kelimeyi a lsitesine atıyorum
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
