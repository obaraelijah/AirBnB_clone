#!/usr/bin/python3
"""
This is the model that provides the base class 
"""
import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage

storage = FileStorage()

class BaseModel():
    """This is a class basemodel that defines all common attributes or methods for other classes
    """
    
    def __init__(self, *args, **kwargs):
        """
        init function
        """
        DATE_TIME_FORMAT='%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key,value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key]=datetime.strptime(
                        value, DATE_TIME_FORMAT
                    )
                elif key[0] == 'id':
                    self.__dict__[key]=str(value)
                elif key != "__class__":
                    self.__dict__[key] = value
        else:
             self.id = str(uuid.uuid4())
             self.created_at = datetime.now()
             self.updated_at = datetime.now()
             storage.new(self)
             
        def __str__(self):
            """
            Returns a sting representtation of the object
            """
            return "[{}] ({}) {}".format(type(self).__name__,self.id, self.__dict__)
        
        def save(self):
            """updates the public instance attribute updated_at with the current datetime
            """
            self.updated_at = datetime.now()
            storage.save()
            
        def to_dict(self):
            """Returns a dictionary containing all all keys/values of __dict__ of the instance
            """
            obj_dict = self.__dict__.copy()
            obj_dict['__class__'] = type(self).__name__()
            obj_dict['created_at'] = obj_dict['created_at'].isoformat()
            obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
            return obj_dict
            