from django import forms
from publicadores.models import Atividade
from publicadores import data_atual, LISTA_MES

mes_anterior = data_atual.month - 1
ano_atual = data_atual.year

class AtividadeForm(forms.Form):
    mes_inicio = forms.ChoiceField(choices=LISTA_MES, initial=mes_anterior)
    ano_inicio = forms.IntegerField(initial=ano_atual)
    mes_fim = forms.ChoiceField(choices=LISTA_MES, initial=mes_anterior)
    ano_fim = forms.IntegerField(initial=mes_anterior)