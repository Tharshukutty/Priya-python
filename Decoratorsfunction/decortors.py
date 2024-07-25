# decortors functions


# get a input from user name,review,star rating using decortor function
# def input_decorator(fun):
#     def wrapper():
#         name=input("enter a name:")
#         review=input("write a review:")

#         while True:
#             try:
#                 star_rating=int(input("give a star rating(1-5):"))
#                 if star_rating<1 or star_rating >5:
#                     raise ValueError("Rating must be between 1 to 5")
#                 break
#             except ValueError as e:
#                 print(e)

#         fun(name, review, star_rating)

#     return wrapper
# @input_decorator
# def process_held(name,review,star_rating):
#     print(f"Thank u for entering in ocean {name}")
#     print(f"Welcome {name}")
#     print(f"your review:{review}")
#     print(f"star rating given:{star_rating} star")
# process_held()


# get a string input from user and  i want to print in uppercase and i want to print the user string and last i want to print in lowercase using decorator function


# def case_decorator(func):
#     def wrapper():
#         user = input("Enter a string: ")
#         upper_case = user.upper()
#         print(f"Uppercase: {upper_case}")
#         func(user)
#         lower_case = user.lower()
#         print(f"Lowercase: {lower_case}")
    
#     return wrapper

# @case_decorator
# def process_held(user):
    
#     pass
# process_held()


