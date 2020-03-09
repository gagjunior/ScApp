from django import forms
from publicadores import data_atual, LISTA_MES

mes_atual = data_atual.month - 1

class AtividadeForm(forms.Form):       
    mes_pesquisa = forms.ChoiceField(choices=LISTA_MES, label='Mês', initial=mes_atual, help_text='Selecione o mês desejado para pesquisar')
    ano_pesquisa = forms.IntegerField(label='Ano', initial=data_atual.year, help_text='Digite o ano desejado para pesquisar')