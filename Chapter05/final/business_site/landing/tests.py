from django.conf import settings
from django.test import TestCase


class Exercise05TestCase(TestCase):
    def test_staticfile_storage_setting(self):
        self.assertEqual(
            str(settings.STATICFILES_STORAGE),
            "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
        )
