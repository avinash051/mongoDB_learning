import pymongo
client = pymongo.MongoClient("mongodb+srv://root:root051@cluster0.dxerf.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data = {
    "name" : "avinash",
    "email id" : "avinashkr051@gmail.com",
    "phone Number": +918895987013,
    "designation": "developer",
    "learning" : "Data Science"
}

"""db1 = client["mongotest"]
coll =db1["test"]
coll.insert_one(data)"""
print(data.values())