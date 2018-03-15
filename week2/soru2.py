k = []
d = []
a = input ("Başlangıç : ")
b = input ( "Son : ")
c = input ( "Cümlenizi veya Kelimenizi Giriniz :")
d += c
k = d

k[int(a):int(b)] = []
L = "".join(k)
print(L)


