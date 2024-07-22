import collections
 
#  counter
# list=["a","b","c"]
# result=collections.Counter(list)
# print(result)

# orderdict
# dict= collections.OrderedDict()
# dict['a']=1
# dict['b']=2
# dict['c']=3
# dict['d']=4
# dict['e']=5
# for i,j in dict.items():
#     print(i,j)

# for delecting and add elements
# dict= collections.OrderedDict()
# dict['a']=1
# dict['b']=2
# dict['c']=3
# dict['d']=4
# dict['e']=5
# dict.pop('a')
# dict["a"]=12
# for i,j in dict.items():
#     print(i,j)


# default dict
# my_dict=collections.defaultdict(int)
# l=[1,2,3,4,2,3,1]
# for i in l:
#     my_dict[i]+=1
# print(my_dict)

# # chainmap
# dict1= {"name":"tharshu"}
# dict2= {"age":20}
# dict3= {"course":"python"}
# dict4= {"duration":"three month"}
# dict5= {"grade":"A"}
# dict=collections.ChainMap(dict1,dict2,dict3,dict4,dict5)
# print(dict)

# named tuple
# tuple = collections.namedtuple('student',["name","age","course","location"])
# res=tuple("tharshu","20","python","ocean academy")
# print(res)

# deque
# que=collections.deque([1,2,3,4,5])
# que.append(12)
# print(que)

# que.appendleft(23)
# print(que)

# que.popleft()
# print(que)