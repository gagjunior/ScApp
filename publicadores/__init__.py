from datetime import datetime
from dateutil.relativedelta import relativedelta

data_atual = datetime.now()

mes_anterior = data_atual + relativedelta(months=-1)
num_mes_anterior = mes_anterior.month
ano_mes_anterior = mes_anterior.year

seis_meses_antes = data_atual + relativedelta(months=-6)
num_seis_meses = seis_meses_antes.month
ano_seis_meses = seis_meses_antes.year


LISTA_MES = (
        (1, 'Janeiro'), (2, 'Fevereiro'), (3, 'Março'), (4, 'Abril'),
        (5, 'Maio'), (6, 'Junho'), (7, 'Julho'), (8, 'Agosto'),
        (9, 'Setembro'), (10, 'Outubro'), (11, 'Novembro'), (12, 'Dezembro')
    )
