class Point: #class name has to be capitalised for first letter
    #pass #data to be provided later
    def __init__(self, x=0, y=0): #self means this method belongs to the class of Point, method belongs to particular class
        self.x = x #this is an instance variable that is accessible by the whole class
        self.y = y
        print("Initialising...")

    def get_info(self, *args): #*args for variable length of argument, args = ["a", "b"]
        #print("({}, {})".format(self.x, self.y))
        print(args)

    def get_data(self, **kwargs): #keyword arguments, variable length
        for key, value in kwargs.items():
            print(key, value)

    def __str__(self):
        return "Point ({}, {})".format(self.x, self.y)

def other_function():
    print("abc")

point_a = Point(5, 10)
print(point_a)
point_b = Point()
print(point_b)

point_b.get_info("a", "b")
point_b.get_info(1, 2, 3, 4, 5, 6)

point_b.get_data(var1 = "123", var2 = "345")
print(type(point_b))

x = 1
y = 1.0
z = "a"
print(type(x), type(y), type(z))

#create first instance/object from class
#point_a = Point() #__init__() is called
#print(point_a)
#point_a.get_info()
#print(point_a.x)

