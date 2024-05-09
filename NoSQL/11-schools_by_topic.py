#!/usr/bin/env python3

"""
    It is a Python function that returns the list of
    school having a specific topic
"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """
        Retrieve all schools that cover a specific topic.

        Args:
            - mongo_collection: A pymongo collection object.
            - topic: The topic to search for.

        Returns:
            - A cursor object containing all schools
            that cover the specified topic.

    """
    return mongo_collection.find({"topics": topic})
