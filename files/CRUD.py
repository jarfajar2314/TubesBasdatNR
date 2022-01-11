import pymongo

class CRUD:
    def __init__(self, dbname):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[dbname]

    def insert(self, collname, data):
        collection = self.db[collname]
        try:
            collection.insert_one(data)
        except:
            print("Failed to add document")
            return False
        else:
            print("Document added.")
            return True

    def delete(self, collname, query):
        collection = self.db[collname]
        print(query)
        try:
            collection.delete_one(query)
        except:
            print("Failed to delete document")
            return False
        else:
            print("Document deleted.")
            return True

    def update(self, collname, old, newdata):
        collection = self.db[collname]
        try:
            collection.update_one(old, newdata)
        except:
            print("Failed to update document")
            return False
        else:
            print("Document updated.")
            return True

    def getCollectionData(self, collname):
        collection = self.db[collname]
        try:
            result = collection.find()
        except:
            return 0
        else:
            return result

    def find(self, collname, query):
        collection = self.db[collname]
        try:
            collection.find_one(query)
        except:
            print("Document not found")
            return False
        else:
            print("Document found.")
            return collection.find_one(query)