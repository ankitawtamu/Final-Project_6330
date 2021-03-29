import unittest
import sqlite3
from unittest import result, mock
from Flaskapp import *
from Flaskapp import app


# using unittest(mock function) to test addbookmark
@mock.patch('Flaskapp.addbookmark')
def addbookmark(self, mock):
    mock = addbookmark
    assert mock is addbookmark

if __name__ == "__main__":
    unittest.main()