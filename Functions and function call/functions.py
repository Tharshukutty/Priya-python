# functions

# functions call

# calculate square
# def calculate_square(number):
    
#     return(number*number)
# num=int(input("enter a number:"))
# square=calculate_square(num)
# print(square)

# Calculate Area of Rectangle
# def Calculate_rectangle_area(length,width):
#     return(length*width)
# length=int(input("enter a number:"))
# width=int(input("enter a number:"))
# area= Calculate_rectangle_area(length,width)
# print(area)

# Check Even or Odd
# def check_even_or_odd(number):
#     if number %2==0:
#         return "even"
#     else:
#         return "odd"
# num=int(input("enter a number:"))
# x=check_even_or_odd(num)
# print(x)

# Calculate Factorial
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# num=int(input("enter a number:"))
# w=factorial(num)
# print(w)

# Reverse a String
# def reverse_str(s):
#     return s[: :-1]
# str1=input("enter a string:")
# reversed_str=reverse_str(str1)
# print(reversed_str)

# Count Characters
# def Count_Characters(s):
#     count={}
#     for char in s:
#         if char in count:
#             count[char]+=1
#         else:
#             count[char]=1
#     return count
# str=input("enter a string:")
# character=Count_Characters(str)
# print(character)

# Sum of Squares
# def Sum_of_Squares(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i*i
#     return sum
# num=int(input("enter a number:"))
# print(Sum_of_Squares(num))


# Check Prime Number
# def prime (n):
#     if n <=1:
#         return False
#     if n <=3:
#         return True
#     if n %2==0 or n %3==0:
#         return False
    
#     i=5
#     while i*i <=n:
#         if  n %i==0 or n %(i+2)==0:
#             return False
#         i += 6
#     return True
# number=int(input("enter a number:"))
# if prime (number):
#     print(f"{number}, is the prime number")
# else:
#     print(f"{number},is not a prime number")


# Check Palindrome using functions
# def is_Palindrome(p):
# # # _Palindrome is a word to reads the same forward or backward
#     p =''.join(char.lower() for char in p if char.isalnum())

#     return p==p [::-1]


# str=input("enter a string:")

# if is_Palindrome(str):
#     print(f'"{str}" is palindrome')
# else:
#     print(f'"{str}" is not palindrome')

# Calculate Fibonacci using function 
# def fibonacci (n):
#     fibonacci_sequence=[]
#     a,b = 0,1
#     for _ in range(n):
#         fibonacci_sequence.append(a)
#         a,b =b,a+b
#     return fibonacci_sequence
# num=int(input("enter a number:"))
# fibonacci_sequence=fibonacci(num)
# print(f"the fibonacci sequence uo to {num} terms:")
# print(fibonacci_sequence)

# Check Armstrong Number
# num=int(input("enter a number:"))
# temp=num
# sum=0
# while temp>0:
#         digits=temp%10
#         cube=digits**3
#         sum=sum+cube
#         temp=temp//10

# if num==sum:
#         print("armstrong number")
# else:
#         print("not a armstrong")

# Check Leap Year
# def is_leap_year(year):
#     if(year%4==0 and year%100!=0)or(year%400==0):
#         return True
#     return False
# test_year=int(input("enter a year:"))
# if is_leap_year(test_year):
#     print(f'{test_year}is a leap year')
# else:
#     print(f'{test_year}is a not leap year')

# check index of duplicate in list

# def find_duplicate_indices(lst):
#     index_dict = {}
#     duplicates = {}
    
#     for index, element in enumerate(lst):
#         if element in index_dict:
#             if element in duplicates:
#                 duplicates[element].append(index)
#             else:
#                 duplicates[element] = [index_dict[element], index]
#         else:
#             index_dict[element] = index
            
#     return duplicates


# test_list = [1,2,3,4,5,5,6,7,8,9]
# duplicate_indices = find_duplicate_indices(test_list)
# print(duplicate_indices)


# list of matrix
# def list_of_matrix (lst1,lst2,lst3):
#     matrix=[]
#     for i in range(len(lst1)):
#         matrix.append([lst1[i]],[lst2[i]],[lst3[i]])

#     return matrix
# lst1=[1,2,3,4]
# lst2=[5,6,7,8]
# lst3=[11,22,33,44]

# print(lst1,lst2,lst3)

# I/P - character, O/P - ascii values / alt keyword 

def get_ascii_value(char):
    return ord(char)

character=input("enter a character:")
print(get_ascii_value(character))