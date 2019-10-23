#!/usr/bin/python3
""" base module """

from json import dumps, loads


class Base:
    """ Base Class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ change from dict to json """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return dumps([])
        else:
            return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves a json to a file """
        obj_list = []
        class_name = cls.__name__
        name_cls = "{}{}".format(class_name, ".json")
        if list_objs:
            for objects in list_objs:
                obj_list.append(objects.to_dictionary())
        with open(name_cls, 'w', encoding='utf-8') as json_file:
            json_file.write(cls.to_json_string(obj_list))

    @classmethod
    def create(cls, **dictionary):
        """ create basic instance """
        if cls.__name__ == "Rectangle":
            basic = cls(1, 1)
        if cls.__name__ == "Square":
            basic = cls(1)
        basic.update(**dictionary)
        return basic

    @staticmethod
    def from_json_string(json_string):
        """ jsonefer """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return loads(json_string)

    @classmethod
    def load_from_file(cls):
        """ loads the file """
        i_list = []
        cls_nm = cls.__name__
        try:
            with open("{}.json".format(cls_nm), encoding='utf-8') as file:
                jsoner = cls.from_json_string(f.read())
                if jsoner is not None or jsoner is not "":
                    for i in jsoner:
                        creator = cls.create(**pointer)
                        i_list.append(creator)
                    return i_list
                return []
        except:
                return []
