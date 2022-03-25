from django.test import TestCase


class Exercise2TestCase(TestCase):
    def test_index_html_content(self):
        """Make sure the static template tag is being used."""
        with open("landing/templates/index.html", "rb") as index_html:
            template_content = index_html.read()

        self.assertIn(
            b"<img src=\"{% static 'landing/logo.png' %}\">", template_content
        )

    def test_index_html_render(self):
        resp = self.client.get("/")

        self.assertIn(b"<h1>Welcome to my Business Site</h1>", resp.content)
        self.assertIn(b'<img src="/static/landing/logo.png">', resp.content)
        self.assertIn(
            b"<p>Welcome to the site for my Business. For all your Business needs!</p>",
            resp.content,
        )
