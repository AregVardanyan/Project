from django.shortcuts import render, redirect
from .models import ArticleField
from core.forms import ArtCreateForm
from django.contrib.auth.models import User


def home_page(request):
    articles = ArticleField.objects.all()
    return render(request, 'core/home.html', {"article_list": articles})


def get_art(request, art_id):
    try:
        art_object = ArticleField.objects.get(id=art_id)
    except ArticleField.DoesNotExist:
        return ("home")
    contex = {
        "art_id": art_id,
        "art_obj": art_object
    }
    return render(request, "core/article_view.html", contex,)


def create_art(request):
    form = ArtCreateForm
    if request.method == "POST":
        form = ArtCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    contex = {'form': form}
    return render(request, "core/new_article.html", contex)


def delete_art(request, art_id):
    try:
        art_object = ArticleField.objects.get(id=art_id)
    except ArticleField.DoesNotExist:
        return redirect("home")
    art_object.delete()
    return redirect("home")


