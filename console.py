#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        return True

    def help_EOF(self):
        print("Exit the program using EOF\n")

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
