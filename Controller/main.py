from Model.file_reader import FileReader
from Model.set_up_class import SetUp


def main():
    """this takes in a file name and pass it to the model"""
    file_name = 'ClassDiagram.txt'
    file_output_name = 'output_file.py'
    SetUp.file_setup_name = file_output_name
    FileReader.file_reader(file_name)


if __name__ == '__main__':
    main()
    import doctest

    doctest.testmod()
