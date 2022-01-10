import pymongo

myclient = pymongo.MongoClient("mongodb+srv://mfajaryusuf:trash_can101@mycluster.3onxd.mongodb.net/test")

# Select db
mydb = myclient["mydatabase"]
# Create collection
mycol = mydb["books"]
# Create dict
mydict = { "name": "Sutan Syahrir", "book": "Pikiran dan Perjuangan","year":"1950" }
# Insert dict to collection
x = mycol.insert_one(mydict)