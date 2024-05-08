#!/usr/bin/env python3

"""
    It is a Python function that changes all topics of
    a school document based on the name
"""


import pymongo


def update_topics(mongo_collection, name, topics):
    """
        Update all topics of a school document based on the name.

        Args:
            - mongo_collection: A pymongo collection object.
            - name: The name of the school to update.
            - topics: A list of strings representing
            the new topics for the school.

        Returns:
            - None
    """
    mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
