from Model.set_up_class import SetUp
from Model.file_reader import FileReader
from View.view_temp import ViewTemp
from Model.test_set_up_class import TestSetUp


class MainController:

    @staticmethod
    def read_data():
        file_name = ViewTemp.get_class_name()
        FileReader.file_reader(file_name)

    @staticmethod
    def write_name():
        file_output_name = ViewTemp.get_output_name()
        SetUp.file_setup_name = file_output_name

    @staticmethod
    def pickle_write_call():
        import pickle
        with open('data.pickle', 'wb') as f:
            pickle.dump(SetUp.uml_list, f)
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
            print(data)

    @staticmethod
    def get_file_data():
        full_data = SetUp.overall_content
        return full_data

    @staticmethod
    def get_unit_test():
        full_test = TestSetUp
        return full_test
