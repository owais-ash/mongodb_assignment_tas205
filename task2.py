import json
import pymongo

mongodb_host = 'localhost'
mongodb_port = 27017
database_name = 'owais'

def load_json_and_insert(collection, json_file_path):
#Loads data from a JSON file and inserts it into the specified MongoDB collection.
    
    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)
            if isinstance(json_data, list):  # Ensuring it's a list of documents as insert_many only possible that way
                collection.insert_many(json_data)
            else:
                collection.insert_one(json_data)
    except Exception as e:
        print(f"An error occurred while loading {json_file_path}: {e}")


# Connect to MongoDB
try:
    client = pymongo.MongoClient(mongodb_host, mongodb_port)
    db = client[database_name]
    
    # Define collections and corresponding JSON file paths
    collections_and_files = {
        'users': 'new_users.json',
        'comments': 'new_comments.json',
        'theaters': 'new_theaters.json',
        'movies': 'new_movies.json'
    }

    # Load JSON data into each collection
    for collection_name, json_file_path in collections_and_files.items():
        load_json_and_insert(db[collection_name], json_file_path)

    print("Data insertion completed successfully.")
finally:
    # Ensure the MongoDB connection is closed even if an error occurs
    client.close()
