#!/usr/bin/python3
"""
The console

Created on: 9th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point of the command interpreter

    Attributes:
        prompt (str): The command line prompt
    """

    prompt = "(hbnb) "

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

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """

        if len(args) == 0:
            print("** class name missing **")
        elif args not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the
        class name and id
        """

        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        """

        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """

        if arg:
            if arg != "BaseModel":
                print("** class doesn't exist **")
                return
            else:
                obj_dict = storage.all(arg)
        else:
            obj_dict = storage.all()

        obj_list = []
        for obj in obj_dict.values():
            obj_list.append(str(obj))

        print(obj_list)


    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """

        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                if args[3].lstrip('-').isdigit():
                    args[3] = int(args[3])
                elif args[3].replace('.', '', 1).lstrip('-').isdigit():
                    args[3] = float(args[3])
                else:
                    args[3] = args[3].strip('"')

                setattr(storage.all()[key], args[2], args[3])  # Set new attribute value
                storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
