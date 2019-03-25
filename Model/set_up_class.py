from Model.file_writer import FileWriter
from Model.replace_value import Replace
from Model.relationship_value import Relationship


class SetUp:
    """The class's docstring
    >>> SetUp.class_dict == {}
    True
    >>> SetUp.file_setup_name == ''
    True
    >>> SetUp.class_relationship == []
    True
    """
    uml_list = []
    class_dict = {}
    class_relationship = []
    attribute_list = []
    method_list = []
    file_setup_name = ''
    overall_content = []

    # {Animals [attribute],[method]}
    # [{'class_name_key', 'value', 'attributes_key', ['', ''], 'methods_key', ['', '']}, {}]

    @staticmethod
    def pass_file():
        FileWriter.file_writer(SetUp.file_setup_name, SetUp.uml_list)


    @staticmethod
    def set_over_string(overall_file):
        """This checks to see if there is a class dict

        """
        # Setup.overall_content = str(overall_file)
        # overall = SetUp.overall_string

        for line in overall_file:
            if ('--' or '..') in line:
                SetUp.set_up_relationship(line)
            elif 'class' in line:
                SetUp.set_up_class_name(line)
            elif ':' in line:
                SetUp.set_up_attribute_name(line)
            elif '(' in line:
                SetUp.set_up_method_name(line)
            elif '}' in line:
                SetUp.class_dict['relationship_key'] = SetUp.class_relationship
                SetUp.class_dict['attributes_key'] = SetUp.attribute_list
                SetUp.class_dict['methods_key'] = SetUp.method_list
                SetUp.overall_content = SetUp.class_dict
                temp_dict = SetUp.class_dict.copy()
                SetUp.uml_list.append(temp_dict)
                SetUp.class_dict.clear()
                SetUp.class_dict = {}
                SetUp.attribute_list = []
                SetUp.method_list = []
            else:
                pass
        SetUp.pass_file()

    @staticmethod
    def set_up_class_name(python_class_name):
        """this returns the class name
        >>> SetUp.set_up_class_name('DiagramModel')
        'DiagramModel'
        >>> SetUp.set_up_class_name('TestModel')
        'TestModel'
        """
        class_name = python_class_name.replace("class", '').replace('{', '')
        SetUp.class_dict['class_name_key'] = class_name
        return class_name

    @staticmethod
    def set_up_attribute_name(attribute_name):
        """This changes String into the str or the diagram
        >>> SetUp.set_up_attribute_name('String data_name:')
        'str  data_name:'
        >>> SetUp.set_up_attribute_name('List id_number:')
        '[]  id_number:'
        >>> SetUp.set_up_attribute_name('Integer count_students:')
        'int  count_students:'
        """
        temp_att = SetUp.clear_up_data(attribute_name)
        at = SetUp.reverse_words(temp_att)
        SetUp.attribute_list.append(at)
        return temp_att

    @staticmethod
    def set_up_method_name(method_name):
        """this removes the String from the method attributes
        >>> SetUp.set_up_method_name('String name')
        ' name'
        """
        temp_met = method_name.replace('void', '')
        met = SetUp.clear_up_data(temp_met).replace('str ', '')
        SetUp.method_list.append(met)
        return met

    @staticmethod
    def set_up_relationship(relationship_value):
        """this method converts diagram to workable class
        >>> SetUp.set_up_relationship('DiagramModel--TestModel')
        'DiagramModel association TestModel'
        """
        temp_rel = SetUp.clean_up_relationship(relationship_value)
        SetUp.class_relationship.append(temp_rel)
        return temp_rel

    @staticmethod
    def clean_up_relationship(relationship):
        """this picks out the right value for the relationship
        >>> SetUp.clean_up_relationship('<|--')
        ' extension '
        >>> SetUp.clean_up_relationship('*--')
        ' composition '
        >>> SetUp.clean_up_relationship('o--')
        ' aggregation '
        >>> SetUp.clean_up_relationship('-->')
        ' directed association '
        >>> SetUp.clean_up_relationship('..|>')
        ' implementation '
        >>> SetUp.clean_up_relationship('..>')
        ' dependency '
        >>> SetUp.clean_up_relationship('<--*')
        ' composition association '
        >>> SetUp.clean_up_relationship('x--')
        ' containment '
        >>> SetUp.clean_up_relationship('}--')
        ' crows feet '
        >>> SetUp.clean_up_relationship('^--')
        ' interface '
        >>> SetUp.clean_up_relationship('..') #I had those last too higher up which failed
        ' inheritance '
        >>> SetUp.clean_up_relationship('--')
        ' association '
        """
        try:
            rel = relationship.replace("<|--", Relationship.EXTENSION.value) \
                .replace('*--', Relationship.COMPOSITION.value) \
                .replace('o--', Relationship.AGGREGATION.value) \
                .replace('-->', Relationship.DIRECTED_ASSOCIATION.value) \
                .replace("..|>", Relationship.IMPLEMENTATION.value) \
                .replace('<--*', Relationship.COMPOSITION_ASSOCIATION.value) \
                .replace('..>', Relationship.DEPENDENCY.value) \
                .replace('x--', Relationship.CONTAINMENT.value) \
                .replace('}--', Relationship.CROWS_FEET.value) \
                .replace('^--', Relationship.INTERFACE.value) \
                .replace("..", Relationship.INHERITANCE.value) \
                .replace("--", Relationship.ASSOCIATION.value)
        except ValueError as error_relationship_data:
            print("the relationship value is:", error_relationship_data)
        except NameError as error_name_relationship_data:
            print("Name of relationship is:", error_name_relationship_data)
        except WrongRelationship as error_relationship_wrong:
            print(error_relationship_wrong)
        except:
            print("An unexpected exception just happened.")
        finally:
            return rel

    @staticmethod
    def clear_up_data(data):
        """this converts to a class diagram str
        >>> SetUp.clear_up_data('String')
        'str '
        >>> SetUp.clear_up_data('Integer')
        'int '
        >>> SetUp.clear_up_data('Float')
        'float '
        >>> SetUp.clear_up_data('Boolean')
        'bool '
        >>> SetUp.clear_up_data('List')
        '[] '
        >>> SetUp.clear_up_data('Tuple')
        '() '
        >>> SetUp.clear_up_data('Dict')
        '{} '
        """
        try:
            clean_data = data.replace('String', Replace.STRING.value) \
                .replace('Integer', Replace.INTEGER.value) \
                .replace('Float', Replace.FLOAT.value) \
                .replace('Boolean', Replace.BOOLEAN.value) \
                .replace('List', Replace.LIST.value) \
                .replace('Tuple', Replace.TUPLE.value) \
                .replace('Dict', Replace.DICT.value) \
                .replace('TestModel', 'TestModel ')
        except ValueError as error_clean_data:
            print("the data cleaning value error is:", error_clean_data)
        except NameError as error_name_clean_data:
            print("Name of data cleaning error is:", error_name_clean_data)
        except DataWrong as error_data_wrong:
            print(error_data_wrong)
        except:
            print("An unexpected exception just happened.")
        finally:
            return clean_data

    @staticmethod
    def reverse_words(word):
        """this reverse words in a string
        >>> SetUp.reverse_words('too word')
        'word too'
        """
        return ' '.join(reversed(word.split()))


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
