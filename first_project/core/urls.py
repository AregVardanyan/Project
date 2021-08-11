from django.urls import path
from core import views

urlpatterns = [
    path('greet/', views.greet,),
    path('intro/', views.intro,),
    path('time/', views.time,),
    path('sqr/', views.sqr, ),
    path('read_js/', views.read_js, ),
]