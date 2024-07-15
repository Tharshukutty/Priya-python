# args*

# sum of all argument
# def sum_of_all_arguments(*args):
#     return sum(args)
# result=sum_of_all_arguments(1,2,3,4,5,6,7,8,9,10)
# print(result)

# Multiply all arguments
# def multiples_of_all_arguments(*args):
#     product=1
#     for i in args:
#       product=product*i
#     return product
# result=multiples_of_all_arguments(1,2,3,4)
# print(result)

# Concatenate all arguments
# def concarenate_all_arguments(*args):
#     result=""
#     for i in args:
#         result+=str(i)
#     return result
# result=concarenate_all_arguments("Thalapathy"," ","Vijay","!",12345)
# print(result)

# arguments and keywords 
# def Print_arguments_and_keywords(*args,**kwargs):
#     print("positional arguments:")
#     for i in args:
#         print(i)
#     print("\nkeywords arguments:")
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")

# Print_arguments_and_keywords(1,2,3,4,5,a=12,s=23,p=30)

# display dictionary content
# def display_dictionary_contents(dict):
#     for key,value in dict.items():
#         print(f"{key}:{value}")
# dict_1={'a':12,'s':23,'p':30}
# display_dictionary_contents(dict_1)

# ************************** LAMBDA FUNCTIONS************************
# Add Two Numbers
# add_number=lambda x,y:x+y
# g=add_number(23,12)
# print(g)

# the Maximum of Two Numbers
# num_max=lambda x,y:x if x>y else y
# a=num_max(12,23)
# print(a)


# Square a Number
# square_number=lambda x: x**2
# a=square_number(3)
# print(a)

