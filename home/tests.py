# from django.test import TestCase
import unittest
from django.core.management import call_command


class MyTests(unittest.TestCase):
    def test_validate_templates(self):
        call_command("validate_templates")
        # This throws an error if it fails to validate
