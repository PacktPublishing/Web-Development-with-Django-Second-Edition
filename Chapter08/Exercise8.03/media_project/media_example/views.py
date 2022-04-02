from django.shortcuts import render
from django.conf import settings


def media_example(request):
    if request.method == "POST":
        save_path = settings.MEDIA_ROOT / request.FILES["file_upload"].name

        with open(save_path, "wb") as output_file:
            for chunk in request.FILES["file_upload"].chunks():
                output_file.write(chunk)

    return render(request, "media-example.html")
