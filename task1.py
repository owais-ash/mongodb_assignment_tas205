import json
import pymongo


# MongoDB connection parameters
mongodb_host = 'localhost'
mongodb_port = 27017
database_name = 'owais'

# Connecting to MongoDB using pymongo
try:
    client = pymongo.MongoClient(mongodb_host, mongodb_port)
    db = client[database_name]

    print("\n\n\tConnection Done\n\n")
    
finally:
    # Ensure the MongoDB connection is closed even if an error occurs
    client.close()
