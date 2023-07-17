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
        """parses an input argument and returns a list of parsed elements"""
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
Usage: show <class_name> <id>, or <class name>.show(<id>)"""
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
        argums = HBNBCommand.parse(arg)
        obdict = models.storage.all()

        if len(argums) == 0:
            print("** class name missing **")
            return False
        if argums[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        if len(argums) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argums[0], argums[1]) not in obdict.keys():
            print("** no instance found **")
            return False
        if len(argums) == 2:
            print("** attribute name missing **")
            return False
        if len(argums) == 3:
            try:
                type(eval(argums[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argums) == 4:
            obj = obdict["{}.{}".format(argums[0], argums[1])]
            if argums[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argums[2]])
                obj.__dict__[argums[2]] = valtype(argums[3])
            else:
                obj.__dict__[argums[2]] = argums[3]
        elif type(eval(argums[2])) == dict:
            obj = obdict["{}.{}".format(argums[0], argums[1])]
            for k, v in eval(argums[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        models.storage.save()

    def do_count(self, arg):
        """Counts the number of instances of a class
Usage: count <class_name>, or <class_name>.count()"""
        argums = HBNBCommand.parse(arg)
        count = 0
        for obj in models.storage.all().values():
            if argums[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, line):
        """default behavior for cmd when input is invalid"""
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = method + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command


if __name__ == '__main__':
    HBNBCommand().cmdloop()
