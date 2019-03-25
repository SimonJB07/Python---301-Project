from cmd import Cmd
from Model.set_up_class import SetUp


class TestData(Cmd):
    """
    single command processor example
    """
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.my_data = SetUp.overall_content

    def do_data(self, the_data):
        """
        Syntax: enter data [the_data]
        Data this can load data to txt file
        :param data: a string representing a class name
        :return: None
        """
        if the_data:
            self.my_data = the_data
        print(self.my_data)

    def do_greet(self, the_data):
        """
        Syntax: greet [the_name]
        Greet the named person
        :param the_data: a string representing a person's name
        :return: None
        """
        if the_data:
            print(the_data)
        else:
            print(self.my_data)

    def do_quit(self):
        print("Quitting, data entry")
        return True

    def help_quit(self):
        print("\n".join(['Quit from my CMD', ':return: True']))

    do_q = do_quit


if __name__ == "__main__":
    test = TestData()
    test.cmdloop()
