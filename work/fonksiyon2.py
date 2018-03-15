def dogru() :
    print ("Tebrikler girdiğiniz şifre doğru ")

def yanlıs() :
    print(" şifre yanlış ")

parola = ("123456")

giris = input("Bir şifre giriniz : ")

if parola == giris :
    dogru()

else :
    yanlıs()