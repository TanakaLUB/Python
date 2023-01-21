import unittest
from unittest import mock


class BookTest(unittest.TestCase):

    def some_function():

        with mock.patch('app.testsample.Book') as book:
            instance = book.return_value
            instance.method.return_value = 'the result1ccc11'
