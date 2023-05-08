#!/usr/bin/python3
"""
A Base class model

Created on: 8th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    A base class that defines all common attributes/methods for other classes.
    """

    def __init__(self):
        """
        Initialize the base model with given values.

        Attributes:
        id (str): Unique identifier for the model instance.
        created_at (datetime.datetime): The date and time the
        instance was created.
        updated_at (datetime.datetime): The date and time the
        instance was last updated.
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the model instance.

        Returns:
            str: A string representation of the model instance.
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Update the updated_at attribute with the current datetime.
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the model instance with
        simple object types.

        Returns:
            dict: A dictionary containing all keys/values of the
            instance's __dict__.
        """

        convert_to_dictionary = self.__dict__.copy()
        convert_to_dictionary["__class__"] = self.__class__.__name__
        convert_to_dictionary["created_at"] = self.created_at.isoformat()
        convert_to_dictionary["updated_at"] = self.updated_at.isoformat()
        return convert_to_dictionary
