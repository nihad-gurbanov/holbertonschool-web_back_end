#!/usr/bin/env python3

"""
    It is a Python function that lists all documents in a collection.
"""

import pymongo


def list_all(mongo_collection):

    """ Retrieve all documents from a MongoDB collection.

        Args:
        - mongo_collection: A pymongo collection object.

        Returns:
        - A cursor object containing all documents in the collection,
        or an empty list if the collection is empty.
    """
    if mongo_collection.count_documents({}) == 0:
        return []
    else:
        return mongo_collection.find()
