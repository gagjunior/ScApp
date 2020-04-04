import uuid
from datetime import date
from django.db import models
from django.urls import reverse
from publicadores import LISTA_MES, num_mes_anterior, ano_mes_anterior

mes_anterior = num_mes_anterior
ano = ano_mes_anterior

class Grupo(models.Model):
    id_grupo = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_grupo = models.CharField(verbose_name='Nome do Grupo', max_length=60)
    dirigente = models.CharField(verbose_name='Dirigente do Gurpo', max_length=60)
    local_grupo = models.CharField(verbose_name='Local do Grupo', max_length=80)
    endereco_grupo = models.TextField(verbose_name='Endereço Grupo', max_length=200, blank=True, null=True)

    DIA_SEMANA = (
        (1, 'Domingo'), (2, 'Segunda'), (3, 'Terça'), (4, 'Quarta'), (5, 'Quinta'), (6, 'Sexta'), (7, 'Sábado')
    )

    dia_saida = models.IntegerField(verbose_name='Dia da Saída', choices=DIA_SEMANA, default=1, blank=True, null=True)    
    horario = models.TimeField(verbose_name='Horário da Saída', blank=True, null=True)
    obs = models.TextField(verbose_name='Observação', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome_grupo

    def get_absolute_url(self):
        return reverse('grupo-detail', args=[str(self.id_grupo)])

    class Meta:
        ordering = ['nome_grupo']
        
# --- Fim do modelo de Grupo ---


class Publicador(models.Model):
    id_publicador = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_publicador = models.CharField(verbose_name='Nome do Publicador', max_length=60)

    GENERO = (
        ('F', 'Feminino'), ('M', 'Masculino')
    )
    genero = models.CharField(verbose_name='Genero', max_length=2, choices=GENERO, default='M')

    data_nascimento = models.DateField(verbose_name='Data de Nascimento', blank=True, null=True)

    ESPERANCA = (
        ('OO', 'Outras Ovelhas'), ('UG', 'Ungido')
    )
    esperanca_pub = models.CharField(verbose_name='Esperança', max_length=2, choices=ESPERANCA, default='OO')

    data_batismo = models.DateField(verbose_name='Data de Batismo', blank=True, null=True)

    ATUACAO = (
        ('Pb', 'Publicador'), ('Pa', 'Pioneiro Auxiliar'), ('Pr', 'Pioneiro Regular'), ('Pes', 'Pioneiro Especial')
    )
    atuacao_pub = models.CharField(verbose_name='Atuação', max_length=3, choices=ATUACAO)

    PRIVILEGIO = (
        ('Sm', 'Servo Ministerial'), ('Ac', 'Ancião')
    )
    privilegio_pub = models.CharField(verbose_name='Privilégio', max_length=2, choices=PRIVILEGIO, blank=True, null=True)

    grupo_pub = models.ForeignKey('Grupo', verbose_name='Grupo Publicador', on_delete=models.DO_NOTHING)
    tel_fixo = models.CharField(verbose_name='Telefone Fixo', max_length=25, blank=True, null=True)
    tel_celular = models.CharField(verbose_name='Telefone Celular', max_length=25, blank=True, null=True)
    endereco_pub = models.TextField(verbose_name='Endereço', max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.nome_publicador

    def get_absolute_url(self):
        return reverse('publicador-detail', args=[str(self.id_publicador)])

    class Meta:
        ordering = ['nome_publicador', 'grupo_pub']

# --- Fim do modelo Publicador ---


class Atividade(models.Model):
    id_atividade = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   
    mes_relatorio = models.IntegerField(verbose_name='Mês', choices= LISTA_MES, default=mes_anterior)
    ano_relatorio = models.IntegerField(verbose_name='Ano', default=ano)
    publicador = models.ForeignKey('Publicador', on_delete=models.DO_NOTHING)
    publicacoes = models.IntegerField(verbose_name='Publicações')
    videos = models.IntegerField(verbose_name='Vídeos')
    horas = models.FloatField(verbose_name='Horas')
    revisitas = models.IntegerField(verbose_name='Revisitas')
    estudos = models.IntegerField(verbose_name='Estudos')
    obs_relatorio = models.TextField(verbose_name='Observação', max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.mes_relatorio}/{self.ano_relatorio} - {self.publicador}'

    def get_absolute_url(self):
        return reverse('atividade-detail', args= [str(self.id_atividade)])

    class Meta:
        ordering = ['mes_relatorio', 'ano_relatorio', 'publicador']