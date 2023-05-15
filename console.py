#!/usr/bin/python3
"""Console Module"""
import cmd
from datetime import datetime
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
        Hbnb command line interface
    """

    classes = [
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
    ]

    # ------------ Class attributes ---------- #
    prompt = '(hbnb) '

    # ------------ Command methods ----------- #
    def do_quit(self, arg):
        """
            Quits command line interface
        """
        return True

    def do_EOF(self, arg):
        """
            Exits command line interface
            after EOF signal
        """
        print()
        return True

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel
        """
        if arg:
            args = arg.split()
            arg = args[0]
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                obj = eval(arg)()
                obj.save()
                print(obj.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance based
            on the class name and id
        """
        from models import storage
        if arg:
            args = arg.split()
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif args[1] not in storage.ids():
                print("** no instance found **")
            else:
                key = f"{args[0]}.{args[1]}"
                objects = storage.all()
                if key not in objects:
                    print("** no instance found **")
                    return
                for obj_key, obj in objects.items():
                    if key == obj_key:
                        print(obj)
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
            Deletes an instances based on the class name and id.
            and save the change into the JSON file.
        """
        from models import storage
        if arg:
            args = arg.split()
            length = len(args)
            if args[0] in self.classes:
                if length == 1:
                    print("** instance id missing **")
                elif args[1] not in storage.ids():
                    print("** no instance found **")
                else:
                    key = f"{args[0]}.{args[1]}"
                    storage.destroy(key)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class
        """
        from models import storage
        if not arg or arg in self.classes:
            all_objects = []
            objects = {}
            objs = storage.all()
            if arg:
                for obj_attr, obj_val in objs.items():
                    if arg in obj_attr:
                        objects[obj_attr] = obj_val
            else:
                objects = objs
            for obj_key, value in objects.items():
                all_objects.append(str(value))
            print(all_objects)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the name and id
        by adding or updating an attribute
        """
        from models import storage
        args = arg.split()
        if '"' in arg:
            new_args = arg.split('"')
            args = new_args[0].split()
            args.append(new_args[1])
        length = len(args)
        if length == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif length == 1:
            print("** instance id missing **")
        elif length == 2:
            if args[1] not in storage.ids():
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif length == 3:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            attr = args[2]
            value = args[3].strip('"')
            storage.update(key, attr, value)

    def do_count(self, arg):
        """
        Counts the number of objects of all or specified
        """
        from models import storage
        if not arg or arg in self.classes:
            all_objects = []
            objects = {}
            objs = storage.all()
            if arg:
                for obj_attr, obj_val in objs.items():
                    if arg in obj_attr:
                        objects[obj_attr] = obj_val
            else:
                objects = objs
            for obj_key, value in objects.items():
                all_objects.append(str(value))
            print(len(all_objects))
        else:
            print("** class doesn't exist **")


    # ----------- Class methods ------------- #
    def emptyline(self):
        """
            Does nothing
        """
        pass

    def parseline(self, line):
        """
        Input line parser
        """
        if '(' in line and ')' in line:
            line_args = line.split('.')
            cls_name = line_args[0]
            command_args = line_args[1].split('(')
            command = command_args[0]
            args_list = command_args[1].split()
            args_list = [arg.strip('",)') for arg in args_list]
            args = " ".join(args_list)
            if len(args) > 0:
                arg = "{} {}".format(cls_name.strip(' '), args)
            else:
                arg = cls_name
            new_line = "{} {}".format(command, arg)
            return (command, arg, new_line)
        else:
            return cmd.Cmd.parseline(self, line)

    # ------------ help methods ------------- #
    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        print("EOF command to exit the program")
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
