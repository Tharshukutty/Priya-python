# polymorphism

# Create a function which acts as two arguments function and also three arguments function
# def add(x,y,z=2):
#     return x+y+z
# print(add(23,30))


# Create a base class called shape withe method area that return 0
# class Shape:
#     def area(self):
#         return 0

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# shape = Shape()
# print("Shape area:", shape.area()) 
# rectangle = Rectangle(2,3)
# print("Rectangle area:", rectangle.area()) 


# create a base class called person with constructor that takes a name as a parameter 
# class person:
#     def __init__(self,name):
#         self.name=name

# class student(person):
#     def __init__(self,name,grade):
#         super().__init__(name)
#         self.grade=grade
#     def display(self):
#         print(f"Name: {self.name},  Grade: {self.grade}")

# objstu=student("tharshu","A")
# objstu.display()