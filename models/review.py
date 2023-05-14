#!/usr/bin/envpython3
"""
A state model

Created on: 14th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    A class Review that inherits from BaseModel

    Attributes:
        place_id (str): A public class attribute for the Review's place id
        user_id (str): A public class attribute for the Review's user id
        text (str): A public class attribute for the Review's text
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """
        The initialisation of the class User

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """

        super().__init__(*args, **kwargs)
