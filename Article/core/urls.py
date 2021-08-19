from django.urls import path
from core import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("view/<int:art_id>", views.get_art, name='view'),
    path("new/", views.create_art, name='new'),
    path("del/<int:art_id>", views.delete_art, name='del')
]
