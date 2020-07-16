# write some code using unitt4est to test our enlarge() function works as desired
'''
Challenges you ran into here:
1. when you import a module within VS Code, the folder has to have
    an __init__.py file
2. when you invoke it in the terminal, you have to call it differently:
    instead of: python test/my_mod_test
    you have to use the following modular invocation:
    python -m test.my_mod_test

Issue: this is a temporary solution to the problem, because you have to go
to the setup.py and make a change to the packages= part of the file. 
    Previously it said: packages=find_packages()
    have to change it to: packages=['my_lambdata6']
If I didn't make that change, people using the Test PyPI could access my test stuff
and I don't want that. 
'''

import unittest
from my_lambdata6.my_mod import enlarge


class TestMyMod(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(7), 700)

if __name__ == '__main__':
    unittest.main()