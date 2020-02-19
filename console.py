#!/usr/bin/python3
"""
Command line interpreter with cmd
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
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
        else:
            list_class = ['BaseModel', 'User', 'Place', 'State',
                          'City', 'Amenity', 'Review']
            line = line.split()
            if line[0] not in list_class:
                print("** class doesn't exist **")
            else:
                model = eval(line[0] + "()")
                print(model.id)
                model.save()

    def do_show(self, line):
        """Prints string rep of an instance
        """
        st = line.replace(' ', '.')
        agmt = line.split()
        if len(line) == 0:
            print('** class name missing **')
        else:
            list_class = ['BaseModel', 'User', 'Place', 'State',
                          'City', 'Amenity', 'Review']
            if agmt[0] not in list_class:
                print("** class doesn't exist **")
            else:
                if (len(agmt) < 2):
                    print('** instance id missing **')
                else:
                    all_objs = storage.all()
                    if st not in all_objs:
                        print('** no instance found **')
                    else:
                        print(all_objs[st])

    def do_destroy(self, line):
        """Deletes an instance based on the class ame and id
        """
        st = line.replace(' ', '.')
        agmt = line.split()

        if len(line) == 0:
            print('** class name missing **')
        else:
            list_class = ['BaseModel', 'User', 'Place', 'State',
                          'City', 'Amenity', 'Review']
            if agmt[0] not in list_class:
                print("** class doesn't exitst **")
            elif len(agmt) < 2:
                print('** instance id missing **')
            else:
                all_objs = storage.all()
                if st not in all_objs:
                    print('** no instance found **')
                else:
                    del all_objs[st]
                    storage.save()

    def do_all(self, line):
        """Prints string rep of all instances
        """
        lis = []
        list_class = ['BaseModel', 'User', 'Place', 'State',
                      'City', 'Amenity', 'Review']
        dic = storage.all()
        if len(line) > 0:
            if line not in list_class:
                print('** class doesn\'t exist **')
            else:
                for key, value in dic.items():
                    key = key.replace('.', ' ')
                    key = key.split()
                    if key[0] == line:
                        lis.append(str(value))
                print(lis)
        else:
            for key, value in dic.items():
                lis.append(str(value))
            print(lis)

    def do_update(self, line):
        """Updates an instance based on the class
        name and id
        """
        list_class = ['BaseModel', 'User', 'Place', 'State',
                      'City', 'Amenity', 'Review']
        all_objs = storage.all()
        if len(line) == 0:
            print('** class name missing **')
        else:
            agmt = shlex.split(line)
            if agmt[0] not in list_class:
                print('** class doesn\'t exist **')
            elif len(agmt) == 1:
                print('** instance id missing **')
            else:
                if (agmt[0] + '.' + agmt[1]) not in all_objs:
                    print('** no instance found **')
                else:
                    if len(agmt) == 2:
                        print('** attribute name missing **')
                    else:
                        if len(agmt) == 3:
                            print('** value missing **')
                        else:
                            all_objs = storage.all()
                            for i in all_objs.keys():
                                if agmt[0] + '.' + agmt[1] == i:
                                    setattr(all_objs[i], agmt[2], agmt[3])
                                    storage.save()

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
