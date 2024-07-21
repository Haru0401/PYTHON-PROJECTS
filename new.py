class demo:

    def __init__(self,a=0,i=9):
        self.real=a
        self.imag=i
    def getData(self):
        print("{0}+{1}j".format(self.real,self.imag))
p=demo(4,9)
p.getData()
o=demo()
o.getData()
class mammel:
    def display(self):
        print("mammel")
class dog(mammel):
    def dog(self):
        print("dog")
d=dog()
d.display()
d.dog()