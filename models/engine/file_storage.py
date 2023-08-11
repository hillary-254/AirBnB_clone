#!/usr/bin/python3
""" This module contains the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}
    __classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                json_data = file.read()
                obj_dict = json.loads(json_data)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    obj_id = key.split('.')[1]
                    class_ = eval(class_name)
                    obj_instance = class_(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

    def _serialize(self, obj):
        """Serialize an object to a dictionary."""
        obj_dict = obj.to_dict()
        return obj_dict

    def _deserialize(self, obj_dict):
        """Deserialize a dictionary to an object."""
        class_name = obj_dict.get('__class__')
        if class_name == 'BaseModel':
            from models.base_model import BaseModel
            return BaseModel(**obj_dict)
        elif class_name == 'User':
            from models.user import User
            return User(**obj_dict)
