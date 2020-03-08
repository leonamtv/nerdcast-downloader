import datetime

def check_day ( today: int ):
    """
    Verifica se o dia passado por parâmetro
    faz parte da semana atual
    """
    date = datetime.date.today()
    inicio_semana = date - datetime.timedelta(date.weekday())
    fim_semana = inicio_semana + datetime.timedelta(6)
    return today >= inicio_semana.day and today <= fim_semana.day


