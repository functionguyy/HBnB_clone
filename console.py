#!/usr/bin/python3
import cmd
import uuid
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
        Hbnb command line interface
    """
    id = 0
    bm_list = [
    ]
    id_list = []

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
            if arg != "BaseModel":
                print("** class doesn't exist **")
            else:
                bm_id = str(uuid.uuid4())
                created_at = datetime.now()
                updated_at = datetime.now()
                HBNBCommand.bm_list.append(
                    {'id': bm_id,
                     'created_at': f'{created_at}',
                     'updated_at': f"{updated_at}",
                     '__class__': "BaseModel"}
                )
                HBNBCommand.id_list.append(bm_id)
                print(bm_id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
            Prints the string representation of an instance based
            on the class name and id
        """
        if arg:
            arg_list = [ar for ar in arg.split()]
            if arg_list[0] != 'BaseModel':
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            elif arg_list[1] not in HBNBCommand.id_list:
                print("** no instance found **")
            else:
                for bm in HBNBCommand.bm_list:
                    if bm['id'] == arg_list[1]:
                        print("[BaseModel]", f"({arg_list[1]})",bm)
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
            Deletes an instances based on the class name and id.
            and save the change into the JSON file.
        """
        if arg:
            arg_list = arg.split()
            length = len(arg_list)
            if arg_list[0] == "BaseModel":
                if length == 1:
                    print("** instance id missing **")
                elif arg_list[1] not in HBNBCommand.id_list:
                    print("** no instance found **")
                else:
                    for i in range(length):
                        if HBNBCommand.bm_list[i]['id'] == arg_list[1]:
                            break
                    del HBNBCommand.bm_list[i]
                    HBNBCommand.id_list.remove(arg_list[1])
            else:
                print("** class doesn't exit **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class
        """
        if not arg or arg == "BaseModel":
            print('[', end="")
            for bm in HBNBCommand.bm_list:
                print(f"\"[BaseModel] ({bm['id']}) {bm}\"", end="")
                if bm != HBNBCommand.bm_list[-1]:
                    print(", ", end="")
            print(']')
        else:
            print("** class doesn't exist **")


    def do_update(self, arg):
        """
        Updates an instance based on the name and id
        by adding or updating an attribute
        """
        arg_list = arg.split()
        length = len(arg_list)
        if length == 0:
            print("** class name missing **")
        elif length == 1:
            if arg_list[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif length == 2:
            if arg_list[1] not in HBNBCommand.id_list:
                print("** no instance found **")
            else:
                print("** attribute name missing **")
        elif length == 3:
                print("** value missing **")
        else:
            for bm in HBNBCommand.bm_list:
                if bm['id'] == arg_list[1]:
                    bm[arg_list[2]] = arg_list[3].strip('"')

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
