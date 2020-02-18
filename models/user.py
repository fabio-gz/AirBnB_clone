#!/usr/bin/python3
from models.base_model import BaseModel
""" Module User - Model base of a class User """


class User(BaseModel):
    """ Class User, public class attributtes:
    email, password, first_name, last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
