import json
import pymongo

mongodb_host = 'localhost'
mongodb_port = 27017
database_name = 'owais'

client = pymongo.MongoClient(mongodb_host, mongodb_port)
db = client[database_name]

#new Comment to be added to our database
new_comment = {
    "movie_name": "Titanic",
    "text": "I am the King of the World",
    "date": "2001-08-25"
}
#python method to add new_comment to comments.json
def insert_comment(new_comment):
    db.comments.insert_one(new_comment) #insert_one function to insert ONE data in json using MongoDB
    print("new comment added successfully")

insert_comment(new_comment)



#new movie data to be added to our database
new_movie = {
    "runtime": 2,
    "title": "Oppenheimer",
    "plot": "Atom Bomb Manufacturing",
    "year": 2023,
    "imdb_rating": 9.2
}
#python method to add new_comment to comments.json
def insert_movie(new_movie):
    db.movies.insert_one(new_movie) #insert_one function to insert ONE data in json using MongoDB
    print("new movie added successfully")

insert_movie(new_movie)



#new theater dataset to be added to our database
new_theater = [
    {
        "name": "INOX",
        "city": "Bangalore",
    },
    {
        "name": "PVR",
        "city": "Patna",
        "state": "Bihar",
        "zipcode": "800014"
    }
]

def insert_theater(new_theater):
    db.theaters.insert_many(new_theater) #insert_many function to insert MULTIPLE data in json using MongoDB
    print("new theater added successfully")

insert_theater(new_theater)



#new user data to be added to our database
new_user = {
    "id": "TAS205",
    "email": "white@field.com",
    "password": "nammaMetro"
}

def insert_user(added_user):
    db.users.insert_one(added_user)
    print("new user added successfully") #insert_one function to insert ONE data in json using MongoDB

insert_user(new_user)



