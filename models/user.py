#!/usr/bin/python3
""" Module User - Model base of a class User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Class User, public class attributtes:
    email, password, first_name, last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
