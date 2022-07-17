import pymongo
client = pymongo.MongoClient("mongodb+srv://pushpendra:pandey1292@cluster0.vqsd8.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"pushpendra",
    "email" : "pushpendra@ineuron.ai",
    "surname" : "pandey"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)