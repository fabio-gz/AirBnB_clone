#!/usr/bin/python3
import uuid
import datetime
from models import storage

class BaseModel:
    """ Class BaseModel of objects """
    def __init__(self, *args, **kwargs):
        if (kwargs):
            for key, value in kwargs.items():
                if (key == 'created_at' or key == 'updated_at'):
                    setattr(self, key,
                            datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    if (key != '__class__'):
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        dic = self.__dict__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return (dic)
