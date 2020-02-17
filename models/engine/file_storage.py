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
        with open(FileStorage.__file_path, mode='w') as f:
            instances = {}
            for key, value in FileStorage.__objects.items():
                instances[key] = value.to_dict()
            f.write(json.dumps(instances))

    def reload(self):
        try:
            with open(FileStorage.__file_path, mode="r") as f:
                dic= json.load(f.read())
                for key, value in dic.items():
                    if key == '__str__':
                        obj.eval(value['__class__'] + "()")
        except:
            print("Puto Error")
