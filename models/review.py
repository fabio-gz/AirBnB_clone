#!/usr/bin/python3
""" Class Review, inheritances of BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class Review, Public Class Attributes:
    place_id, user_id, text.
    """
    place_id = ""
    user_id = ""
    text = ""
