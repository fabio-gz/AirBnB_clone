#!/usr/bin/python3
"""
Base_model module
Structure base of all objects that will be created in different classes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Class BaseModel of objects
    key - value - created_at - updated_at
    """

    def __init__(self, *args, **kwargs):
        """ Method Init of an object """
        for key, value in kwargs.items():
            if (key == 'created_at' or key == 'updated_at'):
                val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, val)
            else:
                if (key != '__class__'):
                    setattr(self, key, value)
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ String representation of a object """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """ Method save to objects """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ method to_dic, create a dictionary of a object """
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return (dic)
