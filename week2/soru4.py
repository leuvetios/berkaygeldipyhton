a = []
s = input("Polidromu denediğiniz kelimeyi veya Cümleyi giriniz : ")
s = a


my_str = s


rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("polidromdur")

else:
    print("polidrom değildir")