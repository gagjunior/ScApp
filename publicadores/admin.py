from publicadores.models import Grupo, Publicador, Atividade
from django.contrib import admin


@admin.register(Grupo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nome_grupo', 'dirigente', 'local_grupo', 'endereco_grupo', 'dia_saida', 'horario', 'obs')


@admin.register(Publicador)
class PublicadorAdmin(admin.ModelAdmin):
    list_display = ('nome_publicador', 'genero', 'data_nascimento', 'esperanca_pub', 'data_batismo', 'atuacao_pub', 'privilegio_pub', 'grupo_pub', 'tel_fixo', 'tel_celular', 'endereco_pub')

    list_filter = ('grupo_pub', 'atuacao_pub', 'privilegio_pub', 'genero')



@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('mes_relatorio', 'ano_relatorio', 'publicador', 'publicacoes', 'videos', 'horas', 'revisitas', 'estudos', 'obs_relatorio')

    list_filter = ('mes_relatorio', 'ano_relatorio', 'publicador')