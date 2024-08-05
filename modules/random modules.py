# random modules
import random
# Generate a random float between 0 and 1
# random_float= random.random()
# print(random_float) 

# Generate a random integer between two numbers
# random_number=random.randint(10,50)
# print(random_number)

# Choose a random element from a list
# lst=[1,2,3,4,5,6,7,8,9,"priya","tharshu","kuttyma"]
# random_item=random.choice(lst)
# print(random_item)

# Shuffle a list in place 
# list=["priya","tharshu","kuttyma",1,2,3,4]
# print(random.shuffle(list))

# Generate a random sample of elements from a list
# lst=[1,2,3,4,5,6,7,8,9,"priya","tharshu","kuttyma"]
# print(random.sample(lst,4))

# Generate a random even number between 0 and 100 
# random_even=random.randrange(0,101,2)
# print(random_even)

# Generate a random odd number between 1 and 99.
# random_odd=random.randrange(0,99,3)
# print(random_odd)

# Generate a random password of length 8 containing letters and digits
# import string
# letters=string.ascii_letters
# digits= string.digits
# all_char=letters+digits
# password_char=[]
# for _ in range(8):
#     random_char=random.choice(all_char)
#     password_char.append(random_char)

# password_str=''.join(password_char)
# print("password:",password_str)

# Generate a random date within the current year 
# import random
# from datetime import datetime, timedelta

# current_year= datetime.now().year

# if current_year %4==0 and (current_year %100 !=0 or current_year %400==0):
#     days_in_year=366
# else:
#     days_in_year=365

# random_day=random.randint(1, days_in_year)
# random_date= datetime(current_year,1,1)+ timedelta(days= random_day -1)
# print(random_date.strftime("%d-%m-%y"))

# **************************************************PUZZLE TASK*********************************************************

# ^^^^^^^^^^^^^***WELCOME TO CHOCOLATE GAME***^^^^^^^^^^^^^^^^^^^^^
# import random
# def select_random_chocolate():
#     chocolates=["dairy milk","kit-kat","munch","fivestar","milkybar","galaxy","perk","snickers","amul chocolate","dark chocolate","tictac","melody","nestle chocolate"]

#     return random.choice(chocolates),chocolates

# def game():
#     selected_chocolate, chocolates = select_random_chocolate()
#     print("CHOCOLATE BOX")
    
#     for chocolate in chocolates:
#         print(chocolate)

#     user_choice =input("select a chocolate:")
#     if user_choice == selected_chocolate:
#         print(f"Congratulations! You selected correct chocolate:{selected_chocolate}")
#         play_again=input("Do you want to play again? (yes/ no):")
#         if play_again.lower()=="yes":
#             game()
#         else:
#             print("Thanks for playing")
#     else:
#         print(f"Wrong choice! the selected chocolate was: {selected_chocolate}.try again")
#         game()

# game()



