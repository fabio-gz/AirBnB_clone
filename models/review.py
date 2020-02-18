#!/usr/bin/python3
from models.base_model import BaseModel
""" Class Review, inheritances of BaseModel """


class Review(BaseModel):
    """ Class Review, Public Class Attributes:
    place_id, user_id, text.
    """
    place_id = ""
    user_id = ""
    text = ""
