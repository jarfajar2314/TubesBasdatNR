import pymongo
from pymongo.errors import ConnectionFailure

# myclient = pymongo.MongoClient("mongodb+srv://mfajaryusuf:trash_can101@mycluster.3onxd.mongodb.net/test")
url = "mongodb+srv://<user>:<qwe123>@mycluster.3onxd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
url = "mongodb://<user>:<qwe123>@mycluster-shard-00-00.3onxd.mongodb.net:27017,mycluster-shard-00-01.3onxd.mongodb.net:27017,mycluster-shard-00-02.3onxd.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-123ipc-shard-0&authSource=admin&retryWrites=true&w=majority"
# myclient = pymongo.MongoClient("mongodb://user:@123456@mycluster-shard-00-00.3onxd.mongodb.net:27017,mycluster-shard-00-01.3onxd.mongodb.net:27017,mycluster-shard-00-02.3onxd.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-123ipc-shard-0&authSource=admin&retryWrites=true&w=majority")
myclient = pymongo.MongoClient(url)
print(myclient.server_info())

try:
   # The ismaster command is cheap and does not require auth.
   myclient.admin.command('ismaster')
except ConnectionFailure:
   print("Server not available")
else:
    print("connected")
# Select db
mydb = myclient["mydatabase"]
# Create collection
mycol = mydb["books"]
# Create dict
mydict = { "name": "Sutan Syahrir", "book": "Pikiran dan Perjuangan","year":"1950" }
# Insert dict to collection
mycol.insert_one(mydict)