from django.http import HttpResponse
from django.shortcuts import render

from .models import Book


def index(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})


def welcome_view(request):
    message = f"<html><h1>Welcome to Bookr!</h1> <p>{Book.objects.count()} books and counting!</p></html>"
    return HttpResponse(message)
