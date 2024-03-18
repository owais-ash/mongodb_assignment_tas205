import json
import pymongo

mongodb_host = 'localhost'
mongodb_port = 27017
database_name = 'owais'

client = pymongo.MongoClient(mongodb_host, mongodb_port)
db = client[database_name]

#4.a. (i) Find top 10 movies with most comments
top_movies = db.comments.aggregate([
    {"$group": { 
        "_id": "$movie_id", # Group by the 'name' field
        "count": {"$sum": 1} # Count the comments for each group
    }},
    {"$sort": {"count": -1}}, #sort, where -1 means in descending order
    {"$limit": 10}, #limit to 10 outputs from top
])

final_movie_result = []  # Initialize list to hold final results

# Iterate over aggregated results to fetch movie titles
for top in top_movies:
    id = top.get("_id").get('$oid')  # Extract movie_id (oid)
    # Find movie title using movie_id in the 'movies' collection
    movie_name = db.movies.find_one({"_id.oid": id}, {'title': 1, '_id': 0})
    count = top.get("count")  # Get the comment count
    # Append tuple of (movie title, comment count) to final results list
    final_movie_result.append((movie_name['title'], count))

print("\n\tTop 10 movies with most comments\n")
for movie in final_movie_result:
    print(movie)
