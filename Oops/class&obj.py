# Oops

# class and object
# class pondy:
#     name=""
#     age=0
#     def beach(self):
#         print("beach")
#     def park(self):
#         print("play...")
#     def foodcourt(self):
#         print("food...")
# **************************object creations*****************************
# obj=pondy()
# obj.beach()
# obj.park()
# obj.foodcourt()
# obj.name="tharshu"
# obj.age=20
# print(obj.name)
# print(obj.age)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$*******constructor functions*********$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# class pondy:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def set(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)

# obj=pondy("priya",20)
# obj.display()
# obj.display()
# obj.set("tharshini",21)


# *************************************************TASK****************************************TASK****************************TASK******************************

# Task_1
# class laptop:
#     def __init__(self,price,process,ram):
#         self.price=price
#         self.process=process
#         self.ram=ram
#     def set(self,price,process,ram):
#         self.price=price
#         self.process=process
#         self.ram=ram
#     def display(self):
#         print(f"laptop_details:")
#         print(f"Price:${self.price}")
#         print(f"Process:{self.process}")
#         print(f"Ram:{self.ram}GB")

# Dell=laptop(1000,"intel i5",6)

# Lenova=laptop(1222,"intel i7",12)

# Hp=laptop(3000,"intel i9",16)


# print("Dell:")
# Dell.display() 

# print("Lenova:")
# Lenova.display()

# print("Hp:")
# Hp.display()


# Task_2

# class student:
#     def __init__(self,name,age,course,fees):
#         self.name=name
#         self.age=age
#         self.course=course
#         self.fees=fees
    
#     def set(self,name,age,course,fees):
#         self.name=name
#         self.age=age
#         self.course=course
#         self.fees=fees

#     def display(self):
#         print(f"student_details:")
#         print(f"NAME:{self.name}")
#         print(f"AGE:{self.age}")
#         print(f"COURSE:{self.course}")
#         print(f"FEES:${self.fees}")

# student_1=student("priya",20,"python",14000) 

# student_2=student("Tharshu",19,"java",15000)

# student_3=student("Ashwin",20,"jv script",20000)

# student_4=student("Ashu",20,"python",10000)

# print("student_1")
# student_1.display()

# print("student_2")
# student_2.display()

# print("student_3")
# student_3.display()

# print("student_4")
# student_4.display()