# class Shop:
#     inv=0
#     item=0
#     def shopitem(self,item):
#         self.item += item
        
        
#     def inventory(inven):
#         Shop.inv += inven

#     def show(self):
#         print(self.item," ",Shop.inv)

# s1 = Shop()
# s1.shopitem(10)
# s1.shopitem(10)
# Shop.inventory(10)
# s1.show()
# s2 = Shop()
# s2.shopitem(10)
# Shop.inventory(10)
# s2.show()

# class A:
#     def __show(self):
#         print("A class")

# class B(A):
#     pass

# b = B()
# b.show()  

class common:
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def display(self):
        print("l = " ,self.l)    
        print("b = " ,self.b)    

    def area(self):
        return self.l * self.b

class Rec(common):
    def __init__(self , l , b):
        super().__init__(l,b)


class Cuboid(common):
    def __init__(self,l,b,h):
        super().__init__(l,b)
        self.h=h
    def display(self):
        super().display()
        print("h= ",self.h) 

    def volume(self):
        return super().area()*self.h


rect= Rec(10,20)
rect.display()
print("area = ", rect.area())
c=  Cuboid(10,20,30)
c.display()
print("volume = ",c.volume())