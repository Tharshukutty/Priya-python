# list task

# even no. & odd no. with separate list
# number=[1,2,3,4,5,6,7,8,9,10]
# even_number=[]
# odd_number=[]
# for num in number:
#     if num%2==0:
#         even_number.append(num)
#     else:
#        odd_number.append(num)

# print("even number:",even_number)
# print("odd number:",odd_number)

# sum of list
# my_list=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in my_list:
#     sum+=i
# print(sum)

# product of list
# list=[1,2,0,3,2,1]
# product=1
# non_zero=False
# for number in list:
#     if number!=0:  
#       product*=number
#       non_zero=True

# if non_zero:
#     print("zero ingonring list:",product)
# else:
#    print("list contains zero")

# duplicate members of a list
# lst = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 5, 6]
# duplicates = []
# for i in range(len(lst)):
#     for j in range(i + 1, len(lst)):
#         if lst[i] == lst[j] and lst[i] not in duplicates:
#             duplicates.append(lst[i])

# print(duplicates)

# largest and smallest number
# lst = [12, 45, 78, 34, 56, 23, 89, 9, 67, 99, 0, 1]
# largest = lst[0]
# smallest = lst[0]
# for num in lst:
#     if num > largest:
#         largest = num

#     if num < smallest:
#         smallest = num
# print("Largest number:", largest)
# print("Smallest number:", smallest)

# reverse list
lst = [1, 2, 3, 4, 5, 6, 9, 8]
length = len(lst)
reversed_lst =[]
for i in range(length - 1, -1, -1):
    reversed_lst.append(lst[i])

print("Original list:", lst)
print("Reversed list:", reversed_lst)
