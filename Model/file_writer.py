

class FileWriter:
    """The class's docstring"""

    @staticmethod
    def file_writer(file_name, overall_content):
        """The method's docstring

        """
        # print(file_output)
        with open(file_name, "w") as output_file:
            for dict_item in overall_content:
                file_output = dict(dict_item)
                print(f"", file=output_file)
                for k, v in file_output.items():
                    if 'class_name_key' in k:
                        print(f"class {v}:", file=output_file)
                    if 'attributes_key' in k:
                        print(f"    def __inti__(self):", file=output_file)
                        for attributes in v:
                            print(f"        self.{attributes}", file=output_file)
                        print(f"        ", file=output_file)
                    if 'methods_key' in k:
                        for methods in v:
                            print(f"    @staticmethod", file=output_file)
                            print(f"    def {methods}:", file=output_file)
                            print(f"        pass\n", file=output_file)

