#!/usr/bin/env python3

"""
    It is a Python script that provides some stats about
    Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


def nginx_log_stats(mongo_collection):
    """
        Calculate statistics about Nginx logs stored in a MongoDB collection.

        Args:
            - mongo_collection: A pymongo collection
            object containing Nginx logs.

        Returns:
            - None

        Prints:
            - The total number of logs in the collection.
            - The number of logs for each HTTP method
            (GET, POST, PUT, PATCH, DELETE).
            - The number of logs with method GET and path /status.

    """
    total_logs = mongo_collection.count_documents({})

    print("{} logs".format(total_logs))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print("    method {}: {}".format(method, count))

    status_check_count = mongo_collection.count_documents(
            {"method": "GET", "path": "/status"}
            )
    print("{} status check".format(status_check_count))


if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    nginx_collection = db.nginx

    nginx_log_stats(nginx_collection)
