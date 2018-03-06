#Değişkene polidrom olan bir kelime yazdık
my_str = 'ses'
#doğruluğunu kesinleştiriyoruz
my_str = my_str.casefold()
#rev_str değişkenine atıyoruz reserved kodu ile tersini alıyoruz
rev_str = reversed(my_str)
#if ile değişkeni kontrol ediyoruz eğer eşitse polidromdur
if list(my_str) == list(rev_str):
    print("polidromdur")
#değilse polidrom değildir
else:
    print("polidrom değildir")
