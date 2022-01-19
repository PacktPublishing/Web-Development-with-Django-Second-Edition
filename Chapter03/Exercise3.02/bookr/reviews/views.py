from django.shortcuts import render


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})


def welcome_view(request):
    return render(request, 'base.html')
