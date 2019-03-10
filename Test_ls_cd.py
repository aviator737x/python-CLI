import unittest
from src.functions import *
import os

class MyTestCase(unittest.TestCase):
    def test_ls_with_no_arguments(self):
        """Tests ls with no arguments"""
        self.assertEqual(Ls("ls").main_method(['ls']), 'Test_ls_cd.py\nREADME.md\nCLI.py\n.gitignore\n.git\n.idea\nsrc\n')

    def test_ls_with_one_argument(self):
        """Tests ls with one argument"""
        self.assertEqual(Ls("ls .").main_method(['ls', ' ', '.']),
                         'Test_ls_cd.py\nREADME.md\nCLI.py\n.gitignore\n.git\n.idea\nsrc\n')



if __name__ == '__main__':
    unittest.main()
