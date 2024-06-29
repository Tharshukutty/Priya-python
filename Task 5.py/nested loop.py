# # nested loop

# # pattern 1
# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print()
# else:
#     print("success")
        
# # pattern 2
# # for i in range(1,6):
# #     for j in range(1,6):
# #         print(i,end="")
# #     print()

# # pattern 3
# # for row in range(5):
# #     for column in range(6):
# #         print(column, end="")
# #     print()

# # pattern 5
# # for i in range(5):
# #     for j in range(5,0,-1):
# #         print(j,end="")
# #     print()

# pattern 6
# num=1
# row=5
# for i in range(5):
#     for j in range(5):
#         print(num,end="")
#         num+=1
#     print()

# # pattern 7
# num=1
# row=5
# for i in range(5):
#     for j in range(5):
#         print(num,end="")
#         num+=2
#     print()


# pattern 35
# row=6
# for i in range(row):
#     for j in range(i):
#         print(i,end="")
#     print('')

# pattern 36
# row=5
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print('')

# PATTERN 26
# ascii_num=65
# row=6
# for i in range(0,6):
#     for j in range(0,i+1):
#         character=chr(ascii_num)
#         print(character,end="")
#         ascii_num+=1
#     print()

# pattern39
row=6
for i in range(row):
    for j in range(i,0,-1):
        print(j,end="")
    print("\r")

# pattern 41
# start=1
# stop=2
# current_num=stop
# for row in range(2,6):
#     for col in range(start,stop):
#         current_num-=1
#         print(current_num,end='')
#     print()
#     start=stop
#     stop+=row
#     current_num=stop

# pattern34
# row=5
# for i in range(0,row):
#     for j in range(0,i+1):
#         print("*",end='')
#     print("\r")


