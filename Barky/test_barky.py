import unittest
from unittest import TestCase, mock, main
from unittest.mock import patch
from barky import clear_screen, get_bookmark_id_for_deletion, get_github_import_options, get_new_bookmark_data, get_option_choice, get_new_bookmark_info, get_user_input, loop, option_choice_is_valid, print_options

'''
unittest.mock is a library for testing in Python.
mock provides a patch() decorator that handles patching module and class level attributes within the scope of a test, along with sentinel for creating unique objects.
When we nest patch decorators the mocks are passed in to the decorated function in the same order they applied (the normal Python order that decorators are applied). This means from the bottom up,
so in the unittest below the mock for module.functionName is passed in first.
'''

class TestBarkyCode(unittest.TestCase):



    @mock.patch('barky.clear_screen')
    def test_clear_screen(self, mock1):
        mock1 = clear_screen
        assert mock1 is clear_screen

    @mock.patch('barky.print_options')
    def test_print_options(self, mock2):
        mock2 = print_options
        assert mock2 is print_options

    @mock.patch('barky.get_option_choice')
    def test_get_option_choice(self, mock3):
        mock3 = get_option_choice
        assert mock3 is get_option_choice  

    @mock.patch('barky.option_choice_is_valid')
    def test_option_choice_is_valid(self, mock4):
        mock4 = option_choice_is_valid
        assert mock4 is option_choice_is_valid  

    @mock.patch('barky.get_user_input')
    def test_get_user_input(self, mock5):
        mock5 = get_user_input
        assert mock5 is get_user_input 

    @mock.patch('barky.get_new_bookmark_data')
    def test_get_new_bookmark_data(self, mock6):
        mock6 = get_new_bookmark_data
        assert mock6 is get_new_bookmark_data    

    
    @mock.patch('barky.get_bookmark_id_for_deletion')
    def test_get_bookmark_id_for_deletion(self, mock7):
        mock7 = get_bookmark_id_for_deletion
        assert mock7 is get_bookmark_id_for_deletion 


    
    @mock.patch('barky.get_github_import_options')
    def test_get_github_import_options(self, mock8):
        mock8 = get_github_import_options
        assert mock8 is get_github_import_options 

    
    @mock.patch('barky.get_new_bookmark_info')
    def test_get_new_bookmark_info(self, mock9):
        mock9 = get_new_bookmark_info
        assert mock9 is get_new_bookmark_info   

    @mock.patch('barky.loop')
    def test_loop(self, mock10):
        mock10 = loop
        assert mock10 is loop                            

    
    

if __name__ == '__main__':
    unittest.manin()

