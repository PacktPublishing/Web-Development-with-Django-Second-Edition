from urllib.request import urlopen
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class Exercise1TestCase(StaticLiveServerTestCase):
    def test_logo_served(self):
        """Test that logo.png is served from the static URL."""
        with open("landing/static/landing/logo.png", "rb") as lf:
            logo_data = lf.read()

        logo_resp = urlopen(f"{self.live_server_url}/static/landing/logo.png")
        self.assertEqual(logo_data, logo_resp.read())
