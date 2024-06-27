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
    format = "%Y-%m-%d %H:%M:%S"
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        
        Attributes:
            id (str): A unique identifier for the instance.
            created_at (datetime): The datetime when the instance was created.
            updated_at (datetime): The datetime when the instance was last updated.
        """

        if kwargs:
            self.id = kwargs.get('id', str(uuid4()))
            created_at_str = kwargs.get('created_at')
            if created_at_str:
                self.created_at = self.from_string_to_datetime(created_at_str)
            else:
                self.created_at = datetime.datetime.now()
            updated_at_str = kwargs.get('updated_at')
            if updated_at_str:
                self.updated_at = self.from_string_to_datetime(updated_at_str)
            else:
                self.updated_at = self.created_at
        else:
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

    @staticmethod
    def from_string_to_datetime(datetime_string1):
        """
        Converts two datetime strings to datetime objects.

        Args:
            datetime_string1 (str): A string representing the created_at datetime.
            datetime_string2 (str): A string representing the updated_at datetime.

        Returns:
            tuple: A tuple containing two datetime objects (created_at, updated_at).
        """
        format = "%Y-%m-%d %H:%M:%S"
        created_at = datetime.datetime.strptime(datetime_string1, format)
        return created_at
