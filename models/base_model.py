#!/usr/bin/python3
import uuid
import datetime


class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        self.update_at = datetime.datetime.now()

    def to_dict(self):
        return { 'id' : self.id,
                 'created_at' : self.created_at.isoformat(),
                 'updated_at': self.updated_at.isoformat()
                 }
