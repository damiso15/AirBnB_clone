#!/usr/bin/envpython3
"""
A state model

Created on: 14th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A class Place that inherits from BaseModel

    Attributes:
        city_id (str): A public class attribute for the Place's city id
        user_id (str): A public class attribute for the Place's user id
        name (str): A public class attribute for the Place's name
        description (str): A public class attribute for the Place's description
        number_rooms (int): A public class attribute for the Place's number of
        rooms
        number_bathrooms (int): A public class attribute for the Place's number
        of bathrooms
        max_guest (int): A public class attribute for the Place's maximum
        number of guest
        price_by_night (int): A public class attribute for the Place's price at
        night
        latitude (float): A public class attribute for the Place's latitude
        longitude (float): A public class attribute for the Place's longitude
        amenity_ids (list): A public class attribute for the Place's amenity id
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """
        The initialisation of the class User

        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """

        super().__init__(*args, **kwargs)
