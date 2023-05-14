#!/usr/bin/env python3
"""
A user model

Created on: 14th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class User that inherits from BaseModel

    Attributes:
        email (str): A public class attribute for the User's email
        password (str): A public class attribute for the User's password
        first_name (str): A public class attribute for the User's first name
        last_name (str): A public class attributes for the User's last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        The initialisation of the class User

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """

        super().__init__(*args, **kwargs)
