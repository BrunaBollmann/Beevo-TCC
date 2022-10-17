from datetime import date, datetime


def dia(x):
    nomes = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    x = datetime.strptime(x, '%Y-%m-%d').date()
    return nomes[x.weekday()]


def meses(x):
    meses = ['Dezembro', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
             'Outubro', 'Novembro']
    x = datetime.strptime(x, '%Y-%m-%d').date()
    return meses[x.month]
