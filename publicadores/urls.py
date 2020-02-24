from django.urls import path
from publicadores import views


urlpatterns = [
    path('', views.index, name='index'),
    path('publicadores', views.PublicadoresListView.as_view(), name='publicadores'),
    path('publicador/<pk>', views.PublicadoresDetailView.as_view(), name='publicador-detail'),
]