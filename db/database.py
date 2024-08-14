import pymongo

My_client = pymongo.MongoClient("mongodb+srv://priyaarul2303g:priya@cluster0.tash2.mongodb.net/")
db=My_client.database_list
collection=db.Engineering_field

# field={"Name":"Ashwin","age":21,"Workingfield":"electrical engineering","salary":"$100000"}
# collection.insert_one(field)

fields=[{"Name":"Ashwin","age":21,"Workingfield":"electrical engineering","salary":"$1000000"},
       {"Name":"priya","age":21,"Workingfield":"chemical engineering","salary":"$200000"},
       {"Name":"Arul","age":22,"Workingfield":"software engineering","salary":"$800000"},
       {"Name":"Malar","age":23,"Workingfield":"Biomedical engineering","salary":"$900000"},
       {"Name":"Tharshu","age":21,"Workingfield":"computer engineering","salary":"$600000"},
       {"Name":"Vijay","age":25,"Workingfield":"Marine engineering","salary":"$300000"},
       {"Name":"Karthick","age":25,"Workingfield":"Automotive engineering","salary":"$200000"},
       {"Name":"Ashu","age":20,"Workingfield":"Agriculture engineering","salary":"$700000"},
       {"Name":"Kamsala","age":27,"Workingfield":"Engery engineering","salary":"$75000"},
       {"Name":"Siddarth","age":29,"Workingfield":"architectural engineering","salary":"$100000"},
       {"Name":"Praveen","age":23,"Workingfield":"Hardware engineering","salary":"$300000"},
       {"Name":"Parama","age":24,"Workingfield":"aerospace engineering","salary":"$400000"},
       {"Name":"Mani","age":28,"Workingfield":"Environmental engineering","salary":"$50000"},
       {"Name":"Sakthi","age":26,"Workingfield":"engineering management","salary":"$200000"},
       {"Name":"Vetrivel","age":27,"Workingfield":"Civil engineering","salary":"$500000"}]
collection.insert_many(fields)
    
# for finding
# res=collection.find_one()
# print(res)

# res=collection.find()
# for i in res:
#     print(i)

# query filter
# my_query={"age":23}
# res=collection.find(my_query)
# for i in res:
#     print(i)

# query={"age":{"$gt":23}}
# res=collection.find(query)
# for i in res:
#     print(i)

# sorting
# res=collection.find().sort("salary",1)
# for i in res:
#     print(i)


# updating
# old={"age":"21"}
# New={"$set":{"age":23}}
# collection.update_one(old,New)
# for i in collection.find():
#     print(i)

# Deleting
# collection.delete_one({"Name":"Ashwin"})

# limiting
# res=collection.find().limit(10)
# for i in res:
#     print(i)