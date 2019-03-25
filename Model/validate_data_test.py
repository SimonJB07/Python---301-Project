

class ValidateData:
    """This just handles the data
    and checks to see if it is all there

     """

    @staticmethod
    def validate_test_loader(test_data):
        """if the data load correctly
        >>> class_name == 'classDiagramModel{'
        'DiagramModel{'
        """
        if ('--' or '..') in test_data:
            pass
        if 'classDiagramModel{' in test_data:
            pass
        elif ':' in test_data:
            pass
        elif '(' in test_data:
            pass
        elif '}' in test_data:
            pass
        else:
            pass





