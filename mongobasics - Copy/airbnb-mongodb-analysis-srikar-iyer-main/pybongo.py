from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pprint

uri = "mongodb+srv://smi6065:ssundeecrainerbobby1@practicedb.fqgpyy1.mongodb.net/?retryWrites=true&w=majority"
#uri = "mongodb+srv://smi6065:ssundeecrainerbobby1@practicedb.fqgpyy1.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
#client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
print(client)
db = client.potato
print(db.list_collection_names)
my_collection=db["listings"]
print("Query 1 \n")
docs = my_collection.find().limit(2) # get the first 2 documents
for doc in docs:
    print(doc)
print("Query 2 \n")
docs1 = my_collection.find().limit(10) # gets the first 10 documents in pretty form
for doc in docs1:
    pprint.pprint(doc)
print("Query 3 \n")
docs2 = my_collection.distinct("host_name") # Find all the unique host_name values
for doc in docs2:
    print(doc)
