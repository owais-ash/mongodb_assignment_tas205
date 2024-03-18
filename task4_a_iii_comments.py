import json
import pymongo
from datetime import datetime

mongodb_host = 'localhost'
mongodb_port = 27017
database_name = 'owais'

client = pymongo.MongoClient(mongodb_host, mongodb_port)
db = client[database_name]

#4.a. (iii) Given a year find the total number of comments created each month in that year
from datetime import datetime
import calendar

def yearly_comments(year, db):
    """
    Prints the total number of comments for each month in the specified year.

    Args:
    - year: The year to aggregate comments for.
    - db: The database connection object.
    """
    # Define the start and end of the year as datetime objects
    year_start = datetime(year, 1, 1)
    year_end = datetime(year + 1, 1, 1)

    # Convert datetime objects to Unix timestamps for comparison
    start_time = int(year_start.timestamp() * 1000)  # MongoDB uses milliseconds
    end_time = int(year_end.timestamp() * 1000)

    # Setup the aggregation pipeline
    pipeline = [
        # Step 1: Filter comments within the year range
        {"$match": {
            "date.$date.$numberLong": {"$gte": str(start_time), "$lt": str(end_time)}
        }},
        # Step 2: Convert string to date and group comments by month
        {"$addFields": {
            "dateConverted": {"$toDate": {"$toLong": "$date.$date.$numberLong"}}
        }},
        {"$group": {
            "_id": {"month": {"$month": "$dateConverted"}},
            "total_comments": {"$sum": 1}
        }},
        # Step 3: Sort by month for chronological order
        {"$sort": {"_id.month": 1}}
    ]

    # Execute the pipeline and convert results to a list
    comments_by_month = list(db.comments.aggregate(pipeline))

    # Print formatted results
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    for result in comments_by_month:
        month_index = result["_id"]["month"]
        print(f"{months[month_index - 1]}: {result['total_comments']} comments")

# Example usage:
print("The total number of comments created each month in the year 2010:")
yearly_comments(2010, db)