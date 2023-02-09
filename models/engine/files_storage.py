#!/usr/bin/python3

"""
Module provides class FilseStorage
"""

import os.path
import json
import copy

class FileStorage:
    """
    This class serializes instances or objects to a JSON file and deserializes JSON file to instances or objects,
    """
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """
        Returns the dictionary __objects
        return a shallow copy of the __objects dictionary, to prevent the caller from modifying the original dictionary. 
        """
        
        return copy.copy(FileStorage.__objects)
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj is None:
            raise TypeError("obj is None")
        cls_name = type(obj).__name__
        """
        creates a string called "cls_name" which is set to the class name of the input object (obj) using type(obj).__name__
        """
        idd = obj.id
        """
        retrieves the "id" attribute of the object (obj.id) and creates a string called "idd" to stor
        """ 
        key = str(cls_name) + '.' + str(idd)
        """
         creates a key string by concatenating "cls_name" and "idd" with a dot separator
        """
        FileStorage.__objects[key] = obj.to_dict()
        """
        method stores the object in the "__objects" dictionary using the key string as the key and the result of calling obj.to_dict() as the value
        """
        
        
    def save(self):
        """
        serializes __objects to JSON file
        """
        js_str = json.dumps(FileStorage.__objects)
        """
        using the json.dumps function to convert the "__objects" dictionary to a JSON-formatted string (stored in the variable "js_str")
        """
        with open(FileStorage.__file_path, 'w', encoding='UTF-8') as fd:
            fd.write(js_str)
            
            
    def reload(self):
        """
        Desirealizes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="UTF-8") as fd:
                js_str = fd.read()
            FileStorage.__objects = json.loads(js_str)
        else:
            print("The file does not exist")
            
        """uses the json.loads function  parse the contents of "js_str" into a dictionary and store it in the "__objects" instance variable. This effectively reloads the deserialized data into the "__objects" dictionary
        """
        