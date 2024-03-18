import json
import pymongo

mongodb_host = 'localhost'
mongodb_port = 27017
database_name = 'owais'

client = pymongo.MongoClient(mongodb_host, mongodb_port)
db = client[database_name]

#4.a. (i) Find top 10 users who made the maximum number of comments
top_10_users= db.comments.aggregate([
    {"$group": { 
        "_id": "$name", # Group by the 'name' field
        "count": {"$sum": 1} # Count the comments for each group
    }},
    {"$sort": {"count": -1}}, #sort, where -1 means in descending order
    {"$limit": 10}, #limit to 10 outputs from top
    {"$project": {"User Name": "$_id", "count": 1, "_id": 0}}  # Format output

])


print("\n\tTop 10 users with maximum number of comments\n")
for user in top_10_users:
    print(f"{user['User Name']}, Total Comments: {user['count']}")
    

top_10_movies = db.comments.aggregate([
     {"$group": { 
        "_id": "$movie_id", # Group by the 'movie_id' field
        "count": {"$sum": 1} # Count the comments for each group
    }},
    {"$sort": {"count": -1}}, #sort, where -1 means in descending order
    {"$limit": 10}, #limit to 10 outputs from top
    {"$project": {"User Name": "$_id", "count": 1, "_id": 0}}  # Format output

])


top_10 = []
print("\n\tTop 10 users with maximum number of comments\n")
movie_info = []
for movie in top_10_movies:
    id = movie.get("_id").get('$oid')
    movie_name=db.movies.find_one({"_id.oid":id},{'title':1,'_id':0})
    count = movie.get("count")
    movie_info.append((movie_name['title'], count))
print("\nTop 10 movies with most comments")
for movie in top_10:
    print(movie)