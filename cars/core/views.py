from django.shortcuts import render, HttpResponse


def show_cars(request):
    return render(request, "core/index.html")


def car1(request):
    return render(request, "core/index1.html")


def car2(request):
    return render(request, "core/index2.html")


def car3(request):
    return render(request, "core/index3.html")


