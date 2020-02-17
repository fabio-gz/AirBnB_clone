#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exit the command line
        """
        return True

    def do_EOF(self, line):
        """Ctrl-d exit
        """
        return True

    def emptyline(self):
        """empty line doesn't execute anything
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
