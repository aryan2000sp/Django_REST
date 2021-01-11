"""
    This file will handle all testing
    done through out the project.

    NOTE:-
        The name of the .py file should
        be test because when we run the
        command 'py manage.py test' it looks
        for the file with name test.py and runs it.
        Also the name name of the function should
        start with test (eg:- def test_someFinction(): )
"""

"""
    Django has buildin class called 
    TestCase that will have some methods 
    associated with the unit testing.
"""
from django.test import TestCase
from app.calc import add

"""
    Now we are write a class that extends the
    TestCase so that we can use the some
    functions from the TestCase.
"""
class CalcTests(TestCase):

    def test_calcAdd(self):
        #Test the calc add() function
        self.assertEqual(add(1,10), 11)
