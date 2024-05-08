#!/usr/bin/env python3

"""
    It is a Python function that inserts a new document in a collection
    based on kwargs.
"""

import pymongo


def insert_school(mongo_collection, **kwargs):

    """
        Insert a new document into a MongoDB collection based
        on keyword arguments.

        Args:
            - mongo_collection: A pymongo collection object.
            - **kwargs: Keyword arguments representing the fields and values
            of the document to be inserted.

        Returns:
            - The _id of the newly inserted document.
    """
    return mongo_collection.insert_one(kwargs).inserted_id
