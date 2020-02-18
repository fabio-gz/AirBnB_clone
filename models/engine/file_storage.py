#!/usr/bin/python3
import json
""" Storage module.
serializes instances to a JSON file and deserializes JSON file to instances
"""


class FileStorage:
    """ Class FileStorage - management of the objects created, saved in a
    JSON file.
    Private Class Attributes: __file_path - __objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Method All
        Return a dictionary with all instances saved
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Method new
        add to __objects all attributes of a new instance
        in format <obj class name>.id: object
        """
        key = (obj.__class__.__name__ + '.' + obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Method Save
        Serialize __objects in a JSON file.
        """
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as f:
            instances = {}
            for key, value in FileStorage.__objects.items():
                instances[key] = value.to_dict()
            json.dump(instances, f)

    def reload(self):
        """ method Reload
        Reload all instances in the JSON files (deserialization)
        and save it in __objects dict
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        dic = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': menity,
               'Review': Review}
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                obj = json.load(f)
                for key, value in obj.items():
                    obj = dic[value['__class__']](**value)
                    key_obj = value['__class__'] + '.' + value['id']
                    FileStorage.__objects[key_obj] = obj
        except:
            pass
