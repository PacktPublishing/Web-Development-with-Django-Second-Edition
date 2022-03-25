from os import getcwd

from django.conf import settings
from django.test import TestCase


class Exercise4TestCase(TestCase):
    def test_static_root_setting(self):
        self.assertEqual(
            str(settings.STATIC_ROOT), f"{getcwd()}/static_production_test"
        )
