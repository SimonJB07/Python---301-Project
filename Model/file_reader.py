from Model.validate_data_test import ValidateData
from Model.set_up_class import SetUp


class FileReader:

    @staticmethod
    def file_reader(file_name):
        """The method's docstring
        """
        overall_file = []
        with open(file_name, 'r') as diagram_file:
            for line in diagram_file:
                temp_line = line.replace('\n', '').replace(' ', '')
                overall_file.append(temp_line)
            SetUp.set_over_string(overall_file)
            ValidateData.validate_test_loader(overall_file)


