

class FileWriter:
    """The class's docstring"""

    @staticmethod
    def file_writer(file_name, overall_content):
        """this writes to a file using dict as kes
        and having the values as the print outs
        the loop steps though each key in dict
        """
        # print(overall_content)
        if type(file_name) == str:
            if type(overall_content) == list:
                if file_name == 'output_file.py':
                    with open(file_name, "w") as output_file:
                        count = 0
                        for dict_item in overall_content:
                            file_output = dict(dict_item)
                            print(f"", file=output_file)
                            for k, v in file_output.items():
                                if 'class_name_key' in k:
                                    print(f"class {v}:", file=output_file)
                                elif 'relationship_key' in k:
                                    print(f"    def __inti__(self):", file=output_file)
                                    if count == 0:
                                        for relationship in v:
                                            print(f"        self.{relationship}", file=output_file)
                                            count += 1
                                elif 'attributes_key' in k:
                                    for attributes in v:
                                        print(f"        self.{attributes}", file=output_file)
                                    print(f"        ", file=output_file)
                                elif 'methods_key' in k:
                                    for methods in v:
                                        print(f"    @staticmethod", file=output_file)
                                        print(f"    def {methods}:", file=output_file)
                                        print(f"        pass\n", file=output_file)
                else:
                    print("ERROR: OUTPUT FILE IS NOT NAMED CORRECTLY")
            else:
                print("ERROR: FILE WRITER: OVERALL DATA: data type is not corrected")
        else:
            print("ERROR: FILE WRITER: FILE NAME: data type is not corrected")
