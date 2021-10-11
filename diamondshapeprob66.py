# konsi claas  konse method ko use kare(multiple inheritance ki bjh se confusion create hota hai)
# java doesnt allow multiple inheritance while c++ and java allows

class A:
    def met(self):
        print("this is a method from class A")

class B(A):
    def met(self):
        print("this is a method from class B")
class C(A):
    def met(self):
        print("this is a method from class C")
class D(B, C):
    def met(self):
        print("this is a method from class D")

a = A()
b = B()
c = C()
d = D()

d.met()

