from django.urls import path
from publicadores import views


urlpatterns = [
    #Url inicial
    path('', views.index, name='index'),

    #Urls referente aos publicadores
    path('publicadores', views.PublicadoresListView.as_view(), name='publicadores'),
    path('publicador/<pk>', views.PublicadoresDetailView.as_view(), name='publicador-detail'),    

    #Urls referente aos grupos
    path('grupos/', views.GruposListView.as_view(), name='grupos'),

    #Urls referente as atividades
    path('atividades/', views.lista_atividades, name='atividades_lista'),
    path('resumo_mes/', views.resumo_mes_betel, name='resumo_mes_betel'),
    path('nao_relatou/', views.lista_nao_relatou, name='lista_nao_relatou'),
    path('lista_inativos/', views.lista_inativos, name='lista_inativos'),
]