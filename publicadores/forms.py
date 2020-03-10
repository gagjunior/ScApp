from django.forms import ModelForm
from publicadores.models import Atividade
from publicadores import data_atual, LISTA_MES

mes_atual = data_atual.month - 1

class AtividadeForm(ModelForm):

    class Meta:
        model = Atividade
        fields = ['mes_relatorio', 'ano_relatorio']