# dictionary

# person={"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"}
# print(person)

# changeable
# person={"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"}
# person["age"]=20
# print(person)

# access item
# person={"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"}
# x=person["name"]
# print(x)

# person={"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"}
# x=person.get("timing")
# print(x)

# person={"name":"tharshu",
        # "age":19,
        # "course":"python",
        # "timing":"6 to 7"}
# print(person.keys())
# print(person.values())
# print(person.items())

# change item
# person={"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"}
# person.update({"name":"priya"})
# print(person)

# add items
# person={"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"}
# person["id.no"]=23
# print(person)

# remove item
# person={"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"}
# (person.popitem())
# print(person)

# person={"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"}
# person.clear()
# print(person)

# loop dictionary
# person={"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"}
# for i in person.items():
#     print(i)

# nested dict
# company={
#     "person 1":{"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"
#         },
#     " person 2":{"name":"priya",
#         "age":20,
#         "course":"python",
#         "timing":"6 to 7"
#         },
#     "person 3":{"name":"ashu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"
#         }
# }
# for i,j in company.items():
#     print(i)
#     for k in j:
#         print(k+":",j[k])


# ************************************ DICTIONARY TASK**************************************
# # 5 EMPLOYES DATA IN NESTED DICTIONARY
# company={
#     "person -1":{"name":"tharshu",
#         "age":19,
#         "course":"python",
#         "timing":"6 to 7"
#         },
#     " person -2":{"name":"priya",
#         "age":20,
#         "course":"python programming",
#         "timing":"6 to 7"
#         },
#     "person -3":{"name":"ashu",
#         "age":19,
#         "course":"python developer",
#         "timing":"6 to 7"
#         },
#     " person -4":{"name":"arul",
#         "age":45,
#         "course":"java",
#         "timing":"6 to 7"
#         },
#     " person -5":{"name":"malar",
#         "age":40,
#         "course":"java script",
#         "timing":"6 to 7"
#         },
#     "person -6":{"name":"ashwin",
#         "age":21,
#         "course":"python fullstock",
#         "timing":"6 to 7"
#         }
# }
# for i,j in company.items():
#     print(i)
#     for k in j:
#         print(k+":",j[k])


#  count characters

str=input("enter a string:")
char_count={}

index=0
while index<len(str):
    character=str[index]

    found= False

for key in str:
    if key==character:
        found=True
        break

    if found:
        char_count[character]+=1
    else:
        char_count[character]=1


    index+=1
       
print(char_count)










