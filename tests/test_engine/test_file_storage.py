#!/usr/bin/python3
"""
Test suite for FileStorage module
"""


from time import sleep
import unittest
import os
from uuid import uuid4
from models.base_model import BaseModel
import json
from models.engine.file_storage import FileStorage
from datetime import datetime

storage = FileStorage()

class TestFileStorage(unittest.TestCase):
    """
    Contains test for storage methods in FileStorage
    """
    def test_multiple_methods(self):
        """
        Test types representation
        """
        FS_dict = FileStorage.__dict__
        FS__path = '_FileStorage__file_path'
        FS__objs = '_FileStorage__objects'
        FS_path = FS_dict[FS__path]
        FS_objs = FS_dict[FS__objs]
        
        #assert types
        """checks that the type of FS_path is a string and that it's not empty. The second assertion checks that the type of FS_objs is a dictionary
        """
        self.assertTrue(type(FS__path) is str and FS__path)
        self.assertTrue(type(FS_dict) is dict)
        
        #assert objects
        """
         use the getattr function to retrieve the values of the __file_path and 
         __objects attributes of the storage object (which is presumably an instance
         of the FileStorage class) and check that they are not empty and that they are equal to the result of calling the all method of the storage object, respectively
        """
        self.assertTrue(getattr(storage, FS__path))
        self.assertTrue(getattr(storage, FS__path) is storage.all())
        
        FS_objs.clear()

         # object registration and persistent __objects dict
         
        oobjs = storage.all()
        oobjs_cp = oobjs.copy()
        obj = BaseModel()
        storage.new(obj)
        
        self.assertTrue(oobjs is storage.all())
        self.assertEqual(len(oobjs.keys()), 1)
        """
        uses a set difference to check that the only key in the dictionary returned by 
        storage.all() is the string 'BaseModel.{obj.id}', where obj.id is the ID of the newly created BaseModel object
        """
        self.assertTrue(set(storage.all().keys()).difference(set(oobjs_cp.keys())) =={'BaseModel.{}'.format(obj.id)})
        
        
        oobjs_cp = oobjs.copy()
        
        # storage.new(obj)
        self.assertTrue(oobjs is storage.all())
        self.assertEqual(oobjs, oobjs_cp)

        """
        BaseModel object is created and passed to storage.new, and the code asserts that the length of oobjs.keys() is now 2.
        """
        obj = BaseModel()
        storage.new(obj)
        self.assertEqual(len(oobjs.keys()), 2)
        
        # check serialization
        oobjs_cp = oobjs.copy()
        storage.save()
        self.assertTrue(os.path.isfile(FS_path))
        with open(FS_path, 'r') as file:
            js_objs = json.load(file)
            self.assertTrue(type(js_objs) is dict)
            self.assertEqual(len(js_objs.keys()), 2)
            self.assertTrue(all(v in oobjs.keys() for v in js_objs.keys()))
        storage.all().clear()
        storage.reload()
        
        # check deserialization
        for k, v in oobjs_cp.items():
            oobjs_cp[k] = v.to_dict()
        oobjs_cp2 = storage.all().copy()
        for k, v in oobjs_cp2.items():
            oobjs_cp2[k] = v.to_dict()
        self.assertEqual(oobjs_cp, oobjs_cp2)
        
        # check no deserialization for absent file
        oobjs_cp = storage.all().copy()
        os.remove(FS_path)
        storage.reload()
        self.assertEqual(oobjs_cp, storage.all())
        
        # automatic registration for instances created with no args
        obj = BaseModel()
        kid = 'BaseModel.{}'.format(obj.id)
        self.assertTrue(kid in storage.all() and storage.all()[kid] is obj)
        sleep(.01)
        now = datetime.utcnow()
        obj.updated_at = now
        obj.save()
        storage.all().clear()
        storage.reload()
        oobjs = storage.all()
        storage.reload()  # insignificant reload
        
        oobjs2 = storage.all()
        # same deserialization
        self.assertEqual(obj.to_dict(), storage.all()[kid].to_dict())
        self.assertFalse(obj is storage.all()[kid].to_dict())

        # args should not be counted towards manual instantiation
        obj = BaseModel(1, 2, 3)
        kid = 'BaseModel.{}'.format(obj.id)
        self.assertTrue(kid in storage.all() and storage.all()[kid] is obj)

        # instances constructed with kwargs are not registered
        obj = BaseModel(id=str(uuid4()), created_at=now.isoformat(),
                        updated_at=now.isoformat())
        kid = 'BaseModel.{}'.format(obj.id)
        self.assertFalse(kid in storage.all())
        self.assertFalse(obj in storage.all().values())


if __name__ == "__main__":
    unittest.main()