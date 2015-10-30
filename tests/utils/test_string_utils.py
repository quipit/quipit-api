from unittest import TestCase

from quipit.utils import ellipsize


class StringUtilsTestCase(TestCase):
    def test_ellipsize_does_nothing_when_string_is_nothing(self):
        self.assertEqual(None, ellipsize(None))
        self.assertEqual('', ellipsize(''))

    def test_ellipsize_does_nothing_to_string_under_length(self):
        self.assertEqual('Test string', ellipsize('Test string', 40))

    def test_ellipsize_cuts_off_string_longer_than_length(self):
        self.assertEqual('Str...', ellipsize('String', 3))
