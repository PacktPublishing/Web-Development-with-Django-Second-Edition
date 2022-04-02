import os
from unittest import mock
from urllib.request import urlopen

from PIL import Image
from django import forms
from django.conf import settings
from django.test import LiveServerTestCase, Client

from media_example.forms import UploadForm
from media_example.views import media_example


class Exercise5Test(LiveServerTestCase):
    def test_form_definition(self):
        """Test that the UploadForm has the correct field."""
        f = UploadForm()
        self.assertIsInstance(f.fields["file_upload"], forms.ImageField)

    def test_form_in_template(self):
        """Test that the form is in the rendered template."""
        c = Client()
        resp = c.get("/media-example/")
        self.assertEquals(resp.status_code, 200)
        self.assertIn(b'<label for="id_file_upload">File upload:</label>', resp.content)
        self.assertIn(
            b'<input type="file" name="file_upload" accept="image/*" required id="id_file_upload">',
            resp.content,
        )

    @mock.patch("media_example.views.render", name="render")
    def test_render_call(self, mock_render):
        """Test that the view calls render with the correct arguments and returns it."""
        request = mock.MagicMock(name="request")
        resp = media_example(request)

        self.assertEquals(resp, mock_render.return_value)
        self.assertEquals(mock_render.call_args[0][0], request)
        self.assertEquals(mock_render.call_args[0][1], "media-example.html")
        self.assertIsInstance(mock_render.call_args[0][2], dict)
        self.assertEquals(len(mock_render.call_args[0][2]), 1)
        self.assertIsInstance(mock_render.call_args[0][2]["form"], UploadForm)

    def test_media_example_upload(self):
        """
        Test the upload functionality to the media_example view. Check it can be downloaded again.
        """
        filename = "cover.jpg"
        save_path = os.path.join(settings.MEDIA_ROOT, filename)

        try:
            c = Client()
            with open(
                os.path.join(settings.BASE_DIR, "fixtures", "cover.jpg"), "rb"
            ) as fp:
                resp = c.post("/media-example/", {"file_upload": fp})
                self.assertEquals(resp.status_code, 200)

            with open(save_path, "rb") as uploaded_fp:
                media_file = urlopen(self.live_server_url + "/media/" + filename)

                self.assertEquals(media_file.read(), uploaded_fp.read())
            thumbnail = Image.open(save_path)

            self.assertTrue(thumbnail.width == 50 or thumbnail.height == 50)
        finally:
            if os.path.exists(save_path):
                os.unlink(save_path)
