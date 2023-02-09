#!/usr/bin/python3
"""
Model provides the class user
"""

from models import base_model

class User(base_model.BaseModel):
    """
    class user that inherits from basemodel
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    """
    super() method is called to invoke the constructor of the parent class (BaseModel). This is done to ensure that the attributes and methods of the BaseModel class are also available to the User class. The *args 
    and **kwargs parameters allow for any additional arguments to be passed to the constructor.
    """ 
    