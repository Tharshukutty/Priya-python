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
# objstu=student("priya","B")
# objstu.display()


# create a base class called vehicle with a method start that print " vehicle started" 
# class Vehicle:
#     def start(self):
#         print("Vehicle started")
    
# class Car(Vehicle):
#     def start(self):
#         print("Car started")

# vehicle=Vehicle()
# vehicle.start()
# car=Car()
# car.start()

# create a base class called employee with properties name and salary & derived class called manager that inherits from employee and adds a property department 
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name 
#         self.salary=salary
# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.department=department
#     def display(self):
#         print(f"Name: {self.name},   Salary: {self.salary},    Department: {self.department}") 
        
# employee=Employee("Ashu",20000)
# manager=Manager("Tharshu",50000,"HR")
# manager.display()



# Create a class called animal with a sound function that prints "Animal makes sounds" .
# create a derived class called dog that inherits from animals and overrides the sounds methods to print "dog barks " .
# create a another function derived class bird that inherits from animal and overrides sound method to print " birds print"

# class Animal:
#     def sound(self):
#         print("Animal makes sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Bird(Animal):
#     def sound(self):
#         print("Birds print")

# animal=Animal()
# dog=Dog()
# bird=Bird()
# dog.sound()
# bird.sound()


