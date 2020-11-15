# Writa a class for calculating area of a triange which have two perameter base and height ,  one constructor , one maethod calculateArea()

class shape:
    def __init__(self , dim1 , dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("I am area method")



class triangle(shape):
 
    def area(self):
        result = 0.5 * self.dim1 * self.dim2
        print("Area of triangle : ",result)

class rectangle(shape):
 
    def area(self):
        result = self.dim1 * self.dim2
        print("Area of Rectangle : ",result)


t = triangle(20,30)
t.area()

r = rectangle(20,30)
r.area()



    