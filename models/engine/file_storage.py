#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = (obj.__class__.__name__ + '.' + obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as f:
            instances = {}
            for key, value in FileStorage.__objects.items():
                instances[key] = value.to_dict()
            json.dump(instances, f)

    def reload(self):
        from models.base_model import BaseModel

        dic = {'BaseModel' : BaseModel}
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                obj = json.load(f)
                for key, value in obj.items():
                    obj = dic[value['__class__']](**value)
                    key_obj = value['__class__'] + '.' + value['id']
                    FileStorage.__objects[key_obj] = obj
        except:
            pass
