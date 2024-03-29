#!/usr/bin/envpython3
"""
A state model

Created on: 14th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    A class State that inherits from BaseModel

    Attributes:
    name (str): A public class attribute for the State's name
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        The initialisation of the class User

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """

        super().__init__(*args, **kwargs)
