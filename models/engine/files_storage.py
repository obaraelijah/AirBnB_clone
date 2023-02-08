#!/usr/bin/python3

"""
Module provides class FilseStorage
"""

import os.path
import json

class FileStorage:
    """
    This class serializes instances or objects to a JSON file and deserializes JSON file to instances or objects,
    """
    
    __file_path = "file.sjon"
    __objects = {}
    
    def all(self):
        """
        Returns the dictionary __objects
        """
        
        return FileStorage.__objects
    
    def new(self, obj):
        """
        
        """