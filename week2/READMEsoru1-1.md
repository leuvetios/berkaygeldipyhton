import random
s = 0

d = 0
arr = [None] * 100
for i in range(1, 100):

    arr[i] = i


arr[0] = random.randint(1, 99)
print(arr)
random.shuffle(arr)
###Buraya kadar sizin kodunuz.
arr3 = {}
#döngü için bunu kullandım.{}

arr2 = []
#boş bir liste açtım
for x in arr :
#bir döngü açarak x=sayacını arr kadar döndürdüm
    if x not in arr3 :
    #bu döngüyle kesin girmesini sağladım arr3[x] = 1 eşitledim
        arr3[x] = 1
    #bu yüzden yukarı girdikten sonra kesinlikle else giricek çünkü eşit değil while TRUE ile 'de ' yapabilirdim burayı
    else :

        if arr3[x] == 1 :
        #arr3[1] == 1 olarak buraya girdi
            arr2.append(x)
            #arr2.(x) index'i buraya attım
        arr3[x] += 1
        # arr3[] 1 artırdım böylelikle index olarak iki sayaç eşit olduğunda arr2 atarak bana çıktısını vericek
print(arr2)


