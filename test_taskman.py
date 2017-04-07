import unittest
from taskman import main

'''
Test cases for taskman.py
'''

class TaskmanChanges(unittest.TestCase):
    def test_it_works(self):
        self.assertEqual(main('taskman.py'), 'Usage Error. Missing Arguments', 'Not working')

    def test_arguments(self):
        self.assertEqual(main('taskman.py status', '{'Version Control': 0, 'Agile Methodology': 0, 'Programming Logic': 0}'), 'Errors')
