a = int(input("please add a number of line you want to print"))
b = bool(int(input("please add 0 for false")))

def star (a, b):
    if  b == true:
        c = 1
        while c<= a:
            print(c* "*")
            c = c + 1

        else:
            while a > 0:
                print(a * "*")
                a = a - 1


star(a, b)
