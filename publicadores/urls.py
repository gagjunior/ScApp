from django.urls import path
from publicadores import views


urlpatterns = [
    path('', views.index, name='index'),
]