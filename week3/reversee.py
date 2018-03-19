class C :
    def my_method(self):
        str = input("Bir cümle ya da kelime giriniz :")
        index = len(str)
        new_str = []
        while index:
            index -= 1
            new_str.append(str[index])
        new2_str = ''.join(new_str)
        print(new2_str)
c = C()
c.my_method()