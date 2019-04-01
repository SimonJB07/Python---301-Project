
class ViewTemp:

    file_path = 'ClassDiagram.txt'
    output_file_name = 'output_file.py'

    @staticmethod
    def get_class_name():
        try:
            return ViewTemp.file_path
        except FileNotFoundError:
            print('FILE NOT FIND ON COMPUTER')
        except Exception as e:
            print(e)

    @staticmethod
    def get_output_name():
        return ViewTemp.output_file_name

