#!/usr/bin/python3
"""
This module contains the BaseModel class used for creating instances
with unique IDs and timestamps for creation and updates.
"""

from uuid import uuid4
import datetime


class BaseModel:
    """
    A base class for all models, providing unique id, creation, and update timestamps.
    """
    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        
        Attributes:
            id (str): A unique identifier for the instance.
            created_at (datetime): The datetime when the instance was created.
            updated_at (datetime): The datetime when the instance was last updated.
        """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: The string representation of the instance, showing the class name,
                 id, and the instance dictionary.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Converts the instance to a dictionary format.

        Returns:
            dict: A dictionary containing all keys/values of the instance's __dict__,
                  with created_at and updated_at as string formatted datetimes, and
                  an additional __class__ key.
        """
        tmp = dict(self.__dict__)
        tmp['created_at'] = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        tmp['updated_at'] = self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        tmp['__class__'] = self.__class__.__name__
        return tmp
