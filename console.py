#!/usr/bin/python3
"""Console module"""""
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
        """Creates a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of a specified instance"""
        args = HBNBCommand.parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes a specified instance"""
        args = HBNBCommand.parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        args = HBNBCommand.parse(arg)
        instances = models.storage.all()
        if len(args) == 0:
            print([str(instance) for instance in instances.values()])
        elif args[0] in HBNBCommand.classes:
            print([str(instance) for instance in instances.values()
                if type(instance).__name__ == args[0]])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an attribute of a specified instance"""
        args = HBNBCommand.parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = models.storage.all()
            if key in instances:
                instance = instances[key]
                setattr(instance, args[2], args[3].strip('"'))
                instance.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
