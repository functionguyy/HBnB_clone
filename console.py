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
from models import storage
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
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                obj = eval(arg + '()')
                obj.save()
                print(obj.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance based
            on the class name and id
        """
        if arg:
            args = arg.split()
            if args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif args[1] not in storage.ids():
                print("** no instance found **")
            else:
                key = f"{args[0]}.{args[1]}"
                objects = storage.all()
                for obj_key, value in objects.items():
                    if obj_key == key:
                        obj_dict = {}
                        for attr, val in value.items():
                            if attr != "__class__":
                                if attr in ["created_at", "updated_at"]:
                                    val = datetime.fromisoformat(val)
                                obj_dict[attr] = val
                        st = "[{}] ({}) {}".format(args[0], args[1], obj_dict)
                        print(st)
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
            Deletes an instances based on the class name and id.
            and save the change into the JSON file.
        """
        if arg:
            args = arg.split()
            length = len(args)
            if args[0] in HBNBCommand.classes:
                if length == 1:
                    print("** instance id missing **")
                elif args[1] not in storage.ids():
                    print("** no instance found **")
                else:
                    key = f"{args[0]}.{args[1]}"
                    storage.destroy(key)
            else:
                print("** class doesn't exit **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class
        """
        if not arg or arg in HBNBCommand.classes:
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
                class_name = value['__class__']
                obj_id = value['id']
                obj_dict = {}
                for attr, val in value.items():
                    if attr != "__class__":
                        if attr in ["created_at", "updated_at"]:
                            val = datetime.fromisoformat(val)
                        obj_dict[attr] = val
                all_objects.append(f"[{class_name}] ({obj_id}) {obj_dict}")
            print(all_objects)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the name and id
        by adding or updating an attribute
        """
        args = arg.split()
        length = len(args)
        if length == 0:
            print("** class name missing **")
        elif length == 1:
            if args[0] not in HBNCommand.classes:
                print("** class doesn't exist **")
            else:
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

    # ----------- Class methods ------------- #
    def emptyline(self):
        """
            Does nothing
        """
        pass

    # ------------ help methods ------------- #
    def help_quit(self):
        print("Quit command to exit the program")
        print()

    def help_EOF(self):
        print("EOF command to exit the program")
        print()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
