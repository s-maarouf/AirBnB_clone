#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
import re
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb) '

    classes = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review",
    }

    def parse(arg):
        curly_braces_match = re.search(r"\{(.*?)\}", arg)
        brackets_match = re.search(r"\[(.*?)\]", arg)

        if curly_braces_match is None:
            if brackets_match is None:
                return [item.strip(",") for item in arg.split()]
            else:
                lexer = arg[:brackets_match.span()[0]].split()
                result_list = [item.strip(",") for item in lexer]
                result_list.append(brackets_match.group())
                return result_list
        else:
            lexer = arg[:curly_braces_match.span()[0]].split()
            result_list = [item.strip(",") for item in lexer]
            result_list.append(curly_braces_match.group())
            return result_list

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF"""
        print("")
        return True

    def emptyline(self):
        """Doesn't execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        Usage: create <class_name>"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            models.storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
Usage: show <class_name>, or <class name>.show(<id>)"""
        argums = HBNBCommand.parse(arg)
        obdict = models.storage.all()
        if len(argums) == 0:
            print("** class name missing **")
        elif argums[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(argums) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argums[0], argums[1]) not in obdict:
            print("** no instance found **")
        else:
            print(obdict["{}.{}".format(argums[0], argums[1])])

    def do_destroy(self, arg):
        """Deletes an instance
Usage: destroy <class_name>, or <class name>.destroy(<id>)"""
        argums = HBNBCommand.parse(arg)
        obdict = models.storage.all()
        if len(argums) == 0:
            print("** class name missing **")
        elif argums[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(argums) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argums[0], argums[1]) not in obdict:
            print("** no instance found **")
        else:
            del obdict["{}.{}".format(argums[0], argums[1])]
            models.storage.save()

    def do_all(self, arg):
        """Prints all instances
Usage: all, or <class_name> all, or <class_name>.all()"""
        argums = HBNBCommand.parse(arg)
        obdict = models.storage.all()
        if len(argums) > 0 and argums[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objv = []
            for obj in obdict.values():
                if len(argums) > 0 and argums[0] == obj.__class__.__name__:
                    objv.append(obj.__str__())
                elif len(argums) == 0:
                    objv.append(obj.__str__())
            print(objv)

    def do_update(self, arg):
        """Updates an instance based on its ID with a dictionary representation
        Usage: update <class_name> <id> <dictionary_representation>"""
        args = HBNBCommand.parse(arg)
        obdict = models.storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(args) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args[0], args[1]) not in obdict.keys():
            print("** no instance found **")
            return False
        if len(args) == 2:
            print("** attribute name missing **")
            return False
        if len(args) == 3:
            try:
                dictionary = eval(args[2])
                if not isinstance(dictionary, dict):
                    raise SyntaxError
            except (NameError, SyntaxError):
                print("** invalid dictionary representation **")
                return False

        obj = obdict["{}.{}".format(args[0], args[1])]
        for key, value in dictionary.items():
            if key in obj.__dict__.keys():
                setattr(obj, key, value)
            else:
                obj.__dict__[key] = value
        obj.save()

    def do_count(self, arg):
        """Counts the number of instances of a class
Usage: count <class_name>, or <class_name>.count()"""
        argums = HBNBCommand.parse(arg)
        count = 0
        for obj in models.storage.all().values():
            if argums[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """default behavior for cmd when input is invalid"""
        argdict = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
