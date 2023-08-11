#!/usr/bin/python3
""" This is the entry point of our program """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    stored_objects = []

    available_classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.available_classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.available_classes[args[0]]()
            self.stored_objects.append(new_instance)
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_found = False
            for instance in self.stored_objects:
                if (type(instance).__name__ == args[0] and
                        instance.id == args[1]):
                    instance_found = True
                    print(str(instance))
            if not instance_found:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            for i, instance in enumerate(self.stored_objects):
                if (type(instance).__name__ == args[0] and
                        instance.id == args[1]):
                    del self.stored_objects[i]
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name."""
        args = arg.split()
        if len(args) > 0:
            if args[0] not in self.available_classes:
                print("** class doesn't exist **")
            else:
                for instance in self.stored_objects:
                    if type(instance).__name__ == args[0]:
                        print(str(instance))
        else:
            for instance in self.stored_objects:
                print(str(instance))

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.available_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            for instance in self.stored_objects:
                if (type(instance).__name__ == args[0] and
                        instance.id == args[1]):
                    setattr(instance, args[2], args[3])
                    return
            print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_help(self, arg):
        """Display help for a given command. USAGE: help [command]"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
