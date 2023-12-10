#!/usr/bin/python3
"""FileStorage"""

import json
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """file storage"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """all"""

        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """new"""

        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """save"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """reload"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                try:
                    self.__objects[key] = classes[jo[key]["__class__"]](
                            **jo[key]
                            )
                except Exception as e:
                    print(f"Error loading object {key}: {e}")
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            print("Error decoding JSON in reload")

    def delete(self, obj=None):
        """delete"""

        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """close"""
        self.reload()
