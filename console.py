#!/usr/bin/python3
"""
The console

Created on: 9th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import cmd
import shlex
import models
import re
import ast
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point of the command interpreter

    Attributes:
        prompt (str): The command line prompt
    """

    prompt = "(hbnb) "
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_quit(self, args):
        """
        Quit command to exit the program
        """

        return True

    def do_EOF(self, args):
        """
        EOF command to exit the program
        """

        return True

    def emptyline(self):
        """
        This will do nothing when receiving empty lines
        """

        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """

        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = models.storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id
        """

        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = models.storage.all()
            if key in all_objs:
                del all_objs[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """

        args = arg.split()
        all_objs = models.storage.all()
        objs_list = []
        if len(args) == 0:
            for value in all_objs.values():
                objs_list.append(str(value))
        elif args[0] in HBNBCommand.classes:
            for key, value in all_objs.items():
                if args[0] in key:
                    objs_list.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(objs_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """

        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in models.storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            updated_obj = models.storage.all()[key]
            setattr(updated_obj, args[2], args[3])
            updated_obj.save()

    def onecmd(self, arg):
        """
        Interpret the command given to the command interpreter
        """
        args = arg.strip("()").split(".")
        if len(args) == 2 and args[1] == "all":
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return False

            all_objs = models.storage.all()
            objs_list = []
            for key, value in all_objs.items():
                if class_name in key:
                    objs_list.append(str(value).replace("\"", ""))
            print(objs_list)

        elif len(args) == 2 and args[1] == "count":
            class_name = args[0]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return False

            all_objs = models.storage.all()
            count = sum(class_name in key for key in all_objs)
            print(count)

        elif len(args) == 2 and "show" in args[1]:
            class_name = args[0]
            instance_id = args[1].split("\"")[1]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return False

            key = class_name + "." + instance_id
            all_objs = models.storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return False

            print(all_objs[key])

        elif len(args) == 2 and "destroy" in args[1]:
            class_name = args[0]
            instance_id = args[1].split("\"")[1]
            if class_name not in self.classes:
                print("** class doesn't exist **")
                return False

            key = class_name + "." + instance_id
            all_objs = models.storage.all()
            if key not in all_objs:
                print("** no instance found **")
                return False

            del all_objs[key]
            models.storage.save()

        elif len(args) == 2 and "update" in args[1]:
            obj = all_objs[key]
            update_dict = ast.literal_eval(dictionary_str)
            for attr_name, attr_val in update_dict.items():
                setattr(obj, attr_name, attr_val)
            obj.save()

        else:
            return super().onecmd(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
