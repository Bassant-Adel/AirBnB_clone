#!/usr/bin/python3
""" Console HBNB """
import cmd
import shlex
import models
from models.city import City
from models.user import User
from datetime import datetime
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNB """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit"""
        return True

    def emptyline(self):
        """ emptyline """
        return False

    def do_quit(self, arg):
        """Quit"""
        return True

    def _key_value_parser(self, args):
        """string"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """Do create"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """Prints the string representation"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name missing **"
                    if len(args) == 0 else "** instance id missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{args[1]}"
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and ID"""
        args = shlex.split(arg)
        if len(args) < 2:
            print("** class name missing **"
                    if len(args) == 0 else "** instance id missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{args[1]}"
	if key in models.storage.all():
	    models.storage.all().pop(key)
            models.storage.save()
	else:
	    print("** no instance found **")

    def do_update(self, arg):
	"""Updates an instance based on the class name and attribute"""
	args = shlex.split(arg)
	if len(args) < 4:
	    print(
	        "** class name missing **" if len(args) == 0 else
		"** instance id missing **" if len(args) == 1 else
		"** attribute name missing **" if len(args) == 2 else
		"** value missing **"
	    )
	    return

	class_name, instance_id, attribute_name, value = args[:4]
	if class_name not in classes:
	    print("** class doesn't exist **")
	    return

	key = f"{class_name}.{instance_id}"
	if key in models.storage.all():
	    instance = models.storage.all()[key]

	    if hasattr(instance, attribute_name):
		value = int(value) if value.isdigit() else float(value)
                if '.' in value else value
	        setattr(instance, attribute_name, value)
		instance.save()
	    else:
		print("** no instance found **")
	else:
	    print("** no instance found **")

    def do_update_dict(self, arg):
        """Updates an instance"""
        args = shlex.split(arg)
        if len(args) < 3:
            print(
                "** class name missing **" if len(args) == 0 else
                "** instance id missing **" if len(args) == 1 else
                "** dictionary missing **"
            )
            return

        class_name, instance_id, dictionary_str = args[:3]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{instance_id}"
        if key in models.storage.all():
            instance = models.storage.all()[key]

            try:
                dictionary = eval(dictionary_str)
            except Exception:
                print("** invalid dictionary **")
                return

            if isinstance(dictionary, dict):
                for key, value in dictionary.items():
                    if hasattr(instance, key):
                        setattr(instance, key, int(value)
                                if str(value).isdigit() else float(value)
                                if '.' in str(value) else value)
                instance.save()
            else:
                print("** invalid dictionary **")
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
