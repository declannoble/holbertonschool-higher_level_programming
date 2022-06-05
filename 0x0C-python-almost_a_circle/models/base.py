#!/usr/bin/python3
"""
Base class module
"""
from fileinput import filename
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialising base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string representation
        of a list of dictionaries
        """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            list_dictionaries = "[]"
            return list_dictionaries

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes JSON string representation of
        list_objs to a file
        """
        list = []
        filename = cls.__name__ + ".json"
        if list_objs:
            for i in list_objs:
                list.append(i.to_dictionary())
        con = cls.to_json_string(list)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(con)

    @staticmethod
    def from_json_string(json_string):
        """
        returns a lsit of the JSON string
        representation: json_string
        """
        if json_string is None or len(json_string) <= 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with
        attributes already set
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        mylist = []
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                mylist = cls.from_json_string(f.read())
                for key, value in enumerate(mylist):
                    mylist[key] = cls.create(**mylist[key])
        except Exception:
            pass
        return mylist
