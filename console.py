#!/usr/bin/python3
"""
This module contains the program for the entry point of the command interpreter

"""

import cmd 


class HBNBCommand(cmd.Cmd):
    """
    The class that the command interpreter operates on.
    
    """
    
    prompt = '(hbnb)'
    class_present=[]
    
    def do_quit(self, arg):
        """
        Quit command used to exit the program
        
        """
        return True
    
    def do_EOF(self, arg):
        """
        
        """
        print("")
        return True
    
    def emptyline(self):
        """
        Prevents the previous command from being executed when empty an empty line is paased.
        """
        pass
    
    def do_create(self, arg):
        """
        Creates a new instance i.e Basemodel saves it (to json) and prints its id.
        Example: $ create BaseModel
        """
        args = list(arg.split())
        if len(args) == 0:
             print("** class name missing **")
             return
        elif args[0] not in HBNBCommand.class_present:
            print("** class doesnt exist **")
            return
        inst = eval(args[0])()
        inst.save()
        print(inst.id)
        
        
    def do_show(self, arg):
        """
        Prints the string representation
        of an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.
        """
        args = list(arg.spilt())
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_present:
            print("** class doesnt exists **")
        elif len(args) == 1:
              print("** instance id missing **")
              return  
        key = args[0] + '.' + args[1]
        if key not in storage.all():
            print("** no instance found **")
        elif HBNBCommand.check_not_id(args[1]):
            print("** no instance found **")
        else:
            key = args[0] + '.' + args[1]
            instances = storage.all().copy()
            inst = eval(args[0])(**instances[key])
            print(inst)
    
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
         (save the change into the JSON file).
         Ex: $ destroy BaseModel 1234-1234-1234.
        """ 
        args = list(arg.split())
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_present():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif HBNBCommand.check_not_id(args[1]):
            print("** no instance found **")
        else:
            key = args[0] + '.' + args[1]
            del storage.all()[key]
            storage.save()
    
    def do_all(self, arg):
        """
         Prints all string representation of all
         instances based or not on the class name.
         Ex: $ all BaseModel or $ all.
        """
        instances = storage.all().copy()
        str_all = []
        args = list(arg.split())
        if len(args) == 0:
            for a_class, info in instances.items():
                inst = eval(info['__class__'])(**info)
                str_all.append(inst.__str__())
        else:
            if args[0] not in HBNBCommand.class_present:
                print("** class doesn't exist **")
                return
            else:
                for a_class, info in instances.items():
                    if info['__class__'] == args[0]:
                        inst = eval(args[0])(**info)
                        str_all.append(inst.__str__())
        print(str_all)
        
    
if __name__ == '__manin__':
    HBNBCommand().cmdloop()