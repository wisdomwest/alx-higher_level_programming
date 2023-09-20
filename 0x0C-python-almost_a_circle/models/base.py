#!/usr/bin/python3
"""Module contains class Base"""

import json
import csv


class Base:
    """This class will be base of all classes"""

    __nb_objects = 0

    def __init__(self, _id=None):
        """Set private attributes id fields"""
        if _id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = _id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON serialization of list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        ordered_keys = ['x', 'width', 'id', 'height', 'y']
        json_list = []

        for dictionary in list_dictionaries:
            ordered_dict = {key: dictionary[key] for key in ordered_keys}
            json_list.append(ordered_dict)

        return json.dumps(json_list)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON serialization of list of objects to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jf.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return class instantied from dictionary of attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return list of classes from JSON strings"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jf:
                list_dicts = Base.from_json_string(jf.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV of list of objects to file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as cf:
            if list_objs is None or list_objs == []:
                cf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(cf, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return list of classes from CSV file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as cf:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(cf, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
