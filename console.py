#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_create(self, line):
        """
        Creates a new instance of the class
        """
        if len(line) == 0:
            print('** class name missing **')
        elif line != 'BaseModel':
            print('** class doesn\'t exist **')
        else:
            line.storage

    def do_show(self, line):
        """
        Prints string rep of an instance
        """
        agmt = line.split()
        if len(line) == 0:
            print('** class name missing **')
        elif line != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(agmt) < 2:
            print('** instance id is missing **')


    def do_quit(self, line):
        """Exit the command line
        """
        return True

    def do_EOF(self, line):
        """Ctrl-d exit
        """
        print('')
        return True

    def emptyline(self):
        """empty line doesn't execute anything
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
