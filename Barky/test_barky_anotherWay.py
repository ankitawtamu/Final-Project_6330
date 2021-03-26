import unittest
from unittest import TestCase
from barky import *
 
class TestCode(unittest.TestCase):

    def test_print_otions(self):
        
        #actualoutput
        actOutput= {"(A) Add a bookmark (B) List bookmarks by date (T) List bookmarks by title (E) Edit a bookmark (D) Delete a bookmark (G) Import GitHub stars (Q) Quit"}
        #expectedoutput
        expOutput=Option.print_options()
        self.assertEqual(actOutput,expOutput)

if __name__ == '__main__':
    unittest.main()        
        