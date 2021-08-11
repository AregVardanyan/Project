from django.shortcuts import HttpResponse, render
from django.utils import timezone
import json


def greet(request):
    return HttpResponse("<h1>Hello:<h1><br>"
                        "<h2>For intro add {/intro} to the current url link:<h2>")


def intro(request):
    return HttpResponse("<h2>Welcome to the page:<h2><br>"
                        "<h3>For time add {/time} to the last url link:<h3><br>"
                        "<h3>For number squares add {/sqr} to the last url link:<h3><br>"
                        "<h3>For reading json file add {/(json file name)} to the last url link:<h3><br>")


def time(request):
    return f"<h2>{timezone.now().date()} {timezone.now().time()}<h2>"


def sqr(request):
    return HttpResponse(f"<h3>{ {i: i **2 for i in range(1, 16)}}<h3><br>"
                        "<h2>For intro add {/intro} to the start url link:<h2>")


def read_js(request):
    with open("name.json", 'r') as js:
        return HttpResponse(f"<h3>{json.load(js)}<h3><br>"
                            "<h2>For intro add {/intro} to the start url link:<h2>")


# Create your views here.
