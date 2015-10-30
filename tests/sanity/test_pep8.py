from subprocess import call
from unittest import TestCase


class PEP8TestCase(TestCase):
    def test_pep8(self):
        checked_dirs = ['tests', 'quipit']
        pep8_command = ['pep8'] + checked_dirs
        if call(pep8_command):
            raise Exception("PEP8 Failed. Check stdout for more information")
