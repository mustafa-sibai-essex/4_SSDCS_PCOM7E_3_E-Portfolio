from cmd import Cmd
from os import listdir


class MyCMD(Cmd):
    """Class that inherits the Cmd class and extends it"""

    prompt = "> "
    intro = "Welcome! Type help to list commands"

    def do_list(self, inp):
        """A function that lists all the content in the current directory"""
        print(listdir())
        return

    def do_add(self, inp):
        """A function that adds two numbers together"""
        numbers = inp.split(" ")
        first_number = int(numbers[0])
        second_number = int(numbers[1])
        addition = first_number + second_number
        print("The result of the number adition is {0}".format(addition))
        return

    def do_help(self, inp):
        """A function that lists all the available commands"""
        print(
            """
list> lists current directory
add> adds two numbers separated with spaces
exit> exits the application"""
        )
        return

    def do_exit(self, inp):
        print("GoodBye!")
        return True


MyCMD().cmdloop()
