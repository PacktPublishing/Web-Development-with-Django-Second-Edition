from urllib.request import urlopen
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class Exercise3TestCase(StaticLiveServerTestCase):
    def test_main_css_loading(self):
        with open("static/main.css", "rb") as cf:
            css_data = cf.read()

        css_resp = urlopen(f"{self.live_server_url}/static/main.css")
        self.assertEqual(css_data, css_resp.read())

    def test_index_html_content(self):
        """Make sure the static template tag is being used."""
        with open("landing/templates/index.html", "rb") as index_html:
            template_content = index_html.read()

        self.assertIn(
            b"<img src=\"{% static 'landing/logo.png' %}\">", template_content
        )
        self.assertIn(
            b'<link rel="stylesheet" href="{% static \'main.css\' %}">',
            template_content,
        )

    def test_index_html_render(self):
        resp = self.client.get("/")

        self.assertIn(b'<link rel="stylesheet" href="/static/main.css">', resp.content)
        self.assertIn(b"<h1>Welcome to my Business Site</h1>", resp.content)
        self.assertIn(b'<img src="/static/landing/logo.png">', resp.content)
        self.assertIn(
            b"<p>Welcome to the site for my Business. For all your Business needs!</p>",
            resp.content,
        )
