# regular expression

# *********************************************************TASK-1***********************************************
# import re

# my_details="my name is Priya, contact number:6385538999, ashutharshu2330@gmail.com, No.30,3rd cross, MGR road, Puduchery-605003."
#  find email id in my_details
# pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2}'
# emails=re.findall(pattern,my_details)
# print("Email.id:",emails)

# find mobile number in my_details
# number = r'\d{10}'
# phone_number = re.findall(number,my_details)
# print("mobile_number:",phone_number)

# find pincode in my_details
# code = r'-\d{6}'
# pincode = re.findall(code,my_details)
# print("pincode:",pincode)

# subtitue the match in my_details
# x = re.sub("Priya","Priyatharshini",my_details)
# print(x)



# *******************************************************TASK-2*******************************************************
import re

# for finding name
# pattern = r'[a-zA-z]'
# Name=input("enter a str:")
# if re.search(pattern,Name):
#     print(f"Name: {Name}")
# else:
#     print("pls enter a valid name")


# for finding email
# pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2}'
# Email=(input("enter a email_id:"))
# if re.search(pattern,Email):
#     print(f"Email_id: {Email}")
# else:
#     print("pls enter a valid email_id")


















