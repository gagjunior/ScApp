from django import forms
from publicadores.models import Atividade
from publicadores import LISTA_MES, num_mes_anterior, ano_mes_anterior, ano_seis_meses, num_seis_meses

mes_anterior = num_mes_anterior
mes_referencia = num_seis_meses # Volta 6 meses atrás
ano_referencia = ano_seis_meses # Volta 6 meses atrás
ano = ano_mes_anterior

class AtividadeForm(forms.Form):
    mes_inicio = forms.ChoiceField(choices=LISTA_MES, initial=mes_anterior)
    ano_inicio = forms.IntegerField(initial=ano)
    mes_fim = forms.ChoiceField(choices=LISTA_MES, initial=mes_anterior)
    ano_fim = forms.IntegerField(initial=ano)

class ResumoForm(forms.Form):
    mes_inicio = forms.ChoiceField(choices=LISTA_MES, initial=mes_anterior)
    ano_inicio = forms.IntegerField(initial=ano)

class NaoRelatouForm(forms.Form):
    mes_inicio = forms.ChoiceField(choices=LISTA_MES, initial=mes_anterior)
    ano_inicio = forms.IntegerField(initial=ano)



