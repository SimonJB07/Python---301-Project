from Controller.main_controller import MainController


def main():
    """this takes in a file name and pass it to the model"""
    MainController.write_name()
    MainController.read_data()
    MainController.get_file_data()


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()



