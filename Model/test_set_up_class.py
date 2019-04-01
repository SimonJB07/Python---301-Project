import unittest
from Model.set_up_class import SetUp


class TestSetUp(unittest.TestCase):
    """unit test that cover some part of the program

    """

    def test_check_string(self):
        """The method's docstring
        """
        print('Test 2')
        result = SetUp.clear_up_data('String')
        self.assertEqual(result, 'str ')

    def test_check_relationship(self):
        """The method's docstring
        """
        print('Test 1')
        result = SetUp.clean_up_relationship('DiagramModelo--TestModel')
        self.assertEqual(result, 'DiagramModel aggregation TestModel')

    def test_reverse_word(self):
        """The method's docstring
        """
        print('Test 3')
        result = SetUp.reverse_words('DiagramModel Good')
        self.assertEqual(result, 'Good DiagramModel')

    def test_set_up_attribute_name(self):
        """The method's docstring

        """
        print('Test 4')
        result = SetUp.set_up_attribute_name('int count_students:')
        self.assertEqual(result, 'int  count_students:')

    def test_set_up_method_name(self):
        """The method's docstring

        """
        print('Test 5')
        result = SetUp.set_up_method_name('void get_name( String name )')
        self.assertEqual(result, ' get_name(  name )')

    def test_set_up_method_name_two(self):
        """The method's docstring

        """
        print('Test 6')
        result = SetUp.set_up_method_name('void set_number_student()')
        self.assertEqual(result, ' set_number_student()')

    def test_set_up_class_name(self):
        """The method's docstring

        """
        print('Test 7')
        result = SetUp.set_up_class_name('classDiagramModel{')
        self.assertEqual(result, 'DiagramModel')


if __name__ == '__main__':
    unittest.main(verbosity=2)
