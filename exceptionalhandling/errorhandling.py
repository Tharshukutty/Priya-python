# exceptional handling

#  the reciprocal of that number. Handle the exception if the user inputs zero

# try:
#         n=float(input("enter a number:"))
#         reciprocal=1/n
#         print(f"the reciprocal {n} is {reciprocal}")
# except ZeroDivisionError:
#         print("zerdivision error, pls enter a non zero number")
# else:
#         print("success")
 
# the reciprocal of that number Handle the exception if the user inputs zero  handle the exception if the user inputs a non-numeric value
# try:
#         n=float(input("enter a number:"))
#         reciprocal=1/n
#         print(f"the reciprocal {n} is {reciprocal}")
# except ZeroDivisionError:
#         print("zerdivision error, pls enter a non zero number")

# except ValueError:
#         print("invalid input,pls enter a numerice value")

# prints its square Use the else clause to print a success message

# try:
#     n=float(input("enter a number:"))
#     square=n**2
#     print(square)
# except Exception as e:
#     print("something wrong, pls enter a numeric value")

# else:
#     print("success")

# prints its square Use the else clause to print a success message and use finally part for message
# try:
#     n=float(input("enter a number:"))
#     square=n**2
#     print(square)
# except Exception as e:
#     print("something wrong, pls enter a numeric value")

# else:
#     print("success")
# finally:
#     print("end of program execution")


# raises a ValueError if the input number is negative

# try:
#     num=float(input("enter a number:"))
#     if num<0:
#         raise ValueError("the number is negative")
#     print(num)
# except Exception as e:
#    print(e)

# repeatedly asks for a number and handles exceptions

# while True:
#     try:
#         num=float(input("enter a number:"))
#         print(f"thank u! you entered a valid number:{num}")
                     
#     except Exception as e:
#         print("invalid input,pls enter a  numeric value")

# raise an exception if user enter string

# while True:
#     user=input("enter a number:")
#     try:
#         num=float(user)
#         print(f"thank u! you entered a vaild number:{num}")
#         break
#     except Exception as e:
#         print("invalid input, pls enter a numeric value",e)