

class ValidateData:
    """This just handles the data
    and checks to see if it is all there
    and load correctly

     """
    @staticmethod
    def validate_test_loader(test_data):
        """if the data load correctly
        >>> class_counter == 2
        2
        >>> relationship_counter == 1
        1
        >>> attribute_counter == 6
        6
        >>> methods_counter == 5
        5
        """
        start = False
        class_counter = 0
        relationship_counter = 0
        methods_counter = 0
        attribute_counter = 0
        class_braced = 0
        end = False

        if type(test_data) == list:
            try:
                for check_line in test_data:
                    if '@startuml' == check_line:
                        start = True
                    elif 'class' in check_line:
                        class_counter += 1
                    elif '--' in check_line:
                        relationship_counter += 1
                    elif ':' in check_line:
                        attribute_counter += 1
                    elif '(' in check_line:
                        methods_counter += 1
                    elif '}' == check_line:
                        class_braced += 1
                    elif '@enduml' == check_line:
                        end = True
            except Exception as e:
                print("ERROR: VALIDATE TEST LOADER CONTENT")
                print(e)
            finally:
                # print(start, end, class_counter)
                return start and end and class_counter == class_braced
        else:
            print("ERROR VALIDATE TEST LOADER: data type is not corrected")
