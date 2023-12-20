#from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "base.html", { "name" : name})


def searchBook(request):
    bookNames = request.GET.get("search") or ""
    return render(request, "searchResult.html", {"books" : bookNames})
