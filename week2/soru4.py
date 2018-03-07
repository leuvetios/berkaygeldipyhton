a = []
s = input("Polidromu denediğiniz kelimeyi veya Cümleyi giriniz : ")


my_str = s

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("polidromdur")

else:
    print("polidrom değildir")