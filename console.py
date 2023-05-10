#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """
        Hbnb command line interface
    """

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
        return True

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel
        """
        if arg:
            if arg != "BaseModel":
                print("** class doesn't exit **")
            else:
                bm = BaseModel()
                bm.save()
                print(bm.id)
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
        else:
            print("** class name missing **")

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
