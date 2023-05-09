#!/usr/bin/python3
"""
The console

Created on: 9th of May, 2023
Authors: Sonaike Oluwadamilola
         Joseph Ocholi
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class contains the entry point of the command interpreter

    Attributes:
        prompt (str): The command line prompt
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """

        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """

        return True

    def emptyline(self):
        """
        This will do nothing when receiving empty lines
        """

        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
