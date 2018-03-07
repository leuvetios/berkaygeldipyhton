

a = []
s = input("Bir cümle yada kelime giriniz : ")
a += s

newList =[ii for n , ii in enumerate(a) if ii not in a[:n]]

d= "".join(newList)
print(d)





