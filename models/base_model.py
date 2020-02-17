#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """ Class BaseModel of objects """
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            if (key == 'created_at' or key == 'updated_at'):
                val = datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%f")
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
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return (dic)