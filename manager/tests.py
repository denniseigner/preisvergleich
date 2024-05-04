from django.test import TestCase


class CiTests(TestCase):
    def test_for_ci(self):
        self.assertIs(True, True)
