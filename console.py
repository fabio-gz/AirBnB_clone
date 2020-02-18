#!/usr/bin/python3
"""
Command line interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """
    Class to manage the command line
    """
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
            model = BaseModel()
            print(model.id)
            model.save()

    def do_show(self, line):
        """Prints string rep of an instance
        """
        agmt = line.split()

        if len(line) == 0:
            print('** class name missing **')
        elif agmt[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(agmt) < 2:
            print('** instance id missing **')
        else:
            all_objs = storage.all()
            for i in all_objs.keys():
                if agmt[0] + '.' + agmt[1] == i:
                    print(all_objs[i])
                    break
                else:
                    print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class ame and id
        """
        agmt = line.split()

        if len(line) == 0:
            print('** class name missing **')
        elif agmt[0] != 'BaseModel':
            print('** class doesn\'t exitst **')
        elif len(agmt) < 2:
            print('** instance id missing **')
        else:
            all_objs = storage.all()
            for i in all_objs.keys():
                if agmt[0] + '.' + agmt[1] == i:
                    del all_objs[i]
                    storage.save()
                    break
                else:
                    print('** no instance found **')

    def do_all(self, line):
        """Prints string rep of all instances
        """
        agmt = line.split()
        list1 = []

        if agmt[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif line == "":
            for key, value in (storage.all()).items():
                list1.append(value)
            print(list1)
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                if key == (line + '.' + value.id):
                    list1.append(value.__str__())
            print(list1)

    def do_update(self, line):
        """Updates an instance based on the class
        name and id
        """
        agmt = shlex.split(line)

        if len(agmt) == 0:
            print('** class name missing **')
        elif agmt[0] != 'BaseModel':
            print('** class doesn\'t exist **')
        elif len(agmt) < 2:
            print('** instance id missing **')
        elif len(agmt) == 2:
            print('** attribute name missing **')
        elif len(agmt) == 3:
            print('** value missing **')
        else:
            all_objs = storage.all()
            for i in all_objs.keys():
                if agmt[0] + '.' + agmt[1] == i:
                    setattr(all_objs[i], agmt[2], agmt[3])
                    storage.save()
                else:
                    print('** no instance found **')

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
