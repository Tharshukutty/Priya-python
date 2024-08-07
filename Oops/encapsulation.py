# encapsulation

# class chocolate:
#     def __init__(self,name):
#         self._name=name

# class dairymilk(chocolate):
#     def __init__(self,name,price):
#         super().__init__(name)
#         self.price=price

# obj=dairymilk("Dairymilk Silk Oreo",65)
# obj._name="Dairymilk Bubbly"
# obj.price=90

# print(obj._name, "$",obj.price)


# # iterators
# my_list=["cherry","apple","banana","mango","watermelon","grapes"]
# x=iter(my_list)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# classes in iterators
# class mynumber:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a<=30:
#             g=self.a
#             self.a +=1
#             return g
#         else:
#             raise StopIteration
# Num=mynumber()
# iter=iter(Num)
# for i in iter:
#     print(i)












