from django.core.cache import cache
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from agendamento.models import *
from agendamento.forms import *
from meses import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/auth/login/')
def index(request):
    if request.user.is_staff:
        staff = 1
    else:
        staff = 0
    if request.method == 'GET':
        input_date = request.GET.get('data')
        periodo = request.GET.get('periodo')
        equipamento = request.GET.get('equipamento')

        if input_date is None:
            input_date = str(timezone.localdate())
        if periodo is None:
            periodo = '1'
        if equipamento is None:
            equipamento = Equipamento.objects.filter(ativo=1).order_by('id')
            equipamento = str(equipamento[0].id)

        if request.GET.get('prox'):
            input_date = datetime.strptime(input_date, '%Y-%m-%d').date()
            input_date += timedelta(days=1)
            input_date = str(input_date)
        elif request.GET.get('ante'):
            input_date = datetime.strptime(input_date, '%Y-%m-%d').date()
            input_date -= timedelta(days=1)
            input_date = str(input_date)

        request.session['data'] = input_date
        request.session['equipamento'] = equipamento
        request.session['periodo'] = periodo

        dados = Agendamento.objects.filter(data=request.session.get('data'),
                                           equipamento_id=request.session.get('equipamento'),
                                           periodo_id=request.session.get('periodo'))

        equip = Equipamento.objects.all().order_by('nome')

        return render(request, 'agendamento/index.html', {'dia_atual': str(request.session.get('data')),
                                                          'id_equipamento': request.session.get('equipamento'),
                                                          'id_periodo': request.session.get('periodo'),
                                                          'dia': input_date[8:10],
                                                          'mes': meses(input_date),
                                                          'dia_semana': dia(input_date),
                                                          'form': AgendarForm,
                                                          'form_equip': equip,
                                                          'aula1': dados.filter(aula_id='1'),
                                                          'aula2': dados.filter(aula_id='2'),
                                                          'aula3': dados.filter(aula_id='3'),
                                                          'aula4': dados.filter(aula_id='4'),
                                                          'aula5': dados.filter(aula_id='5'),
                                                          'aula6': dados.filter(aula_id='6'),
                                                          'aula7': dados.filter(aula_id='7'),
                                                          'aula8': dados.filter(aula_id='8'),
                                                          'usuario': request.user.id,
                                                          'staff': staff})


@login_required(login_url='/auth/login/')
def agendamento(request, id):
    if request.user.is_staff:
        staff = 1
    else:
        staff = 0
    if request.method == 'GET':
        get_equipamento = request.session.get('equipamento')
        equip = Equipamento.objects.filter(id=get_equipamento, ativo=0)
        print(equip)
        if len(equip) == 1:
            return render(request, 'error/equip_manutencao.html')
        get_data = request.session.get('data')
        get_aula = int(id)
        get_periodo = request.session.get('periodo')
        get_responsavel = request.user.id
        periodo = Periodo.objects.get(id=get_periodo)
        equipamento = Equipamento.objects.get(id=get_equipamento)

        if request.GET.get('verificar'):
            if len(Agendamento.objects.filter(data=get_data, aula_id=get_aula, equipamento_id=get_equipamento,
                                              periodo_id=get_periodo)) > 0:
                return render(request, 'error/agendamento_error.html')
            else:
                new = Agendamento(data=get_data,
                                  motivo=request.GET.get('motivo'),
                                  aula_id=get_aula,
                                  equipamento_id=get_equipamento,
                                  periodo_id=get_periodo,
                                  responsavel_id=get_responsavel,
                                  sala_id=request.GET.get('sala'))
                new.save()
                return redirect(f'/?data={request.session.get("data")}&periodo={request.session.get("periodo")}'
                                f'&equipamento={request.session.get("equipamento")}')

        return render(request, 'agendamento/agendamento.html', {'aula': get_aula,
                                                                'form': AgendarForm,
                                                                'data': get_data,
                                                                'periodo': periodo,
                                                                'equipamento': equipamento,
                                                                'staff': staff})


@login_required(login_url='/auth/login/')
def excluir(request, id):
    if request.user.is_staff:
        staff = 1
    else:
        staff = 0
    get_data = request.session.get('data')
    get_aula = int(id)
    get_equipamento = request.session.get('equipamento')
    get_periodo = request.session.get('periodo')
    periodo = Periodo.objects.get(id=get_periodo)
    equipamento = Equipamento.objects.get(id=get_equipamento)
    sala = Agendamento.objects.get(aula_id=get_aula, periodo_id=get_periodo, equipamento_id=get_equipamento,
                                   data=get_data).sala

    if request.method == 'GET':
        if len(Agendamento.objects.filter(data=get_data, periodo_id=get_periodo, equipamento_id=get_equipamento,
                                          aula_id=get_aula, responsavel_id=request.user.id)) == 0:
            return redirect('/')
        else:
            return render(request, 'agendamento/excluir.html', {'aula': get_aula,
                                                                'form': AgendarForm,
                                                                'data': get_data,
                                                                'periodo': periodo,
                                                                'equipamento': equipamento,
                                                                'sala': sala,
                                                                'staff': staff})
    else:
        bd = Agendamento.objects.filter(data=get_data, periodo_id=get_periodo, equipamento_id=get_equipamento,
                                        aula_id=get_aula, responsavel_id=request.user.id)
        bd.delete()
        return redirect(f'/?data={request.session.get("data")}&periodo={request.session.get("periodo")}'
                        f'&equipamento={request.session.get("equipamento")}')


def instrucao(request):
    return render(request, 'instrucao/index.html')


def page_not_found_view(request, exception):
    return render(request, 'error/404.html', status=404)


def handler500(request):
    return render(request, 'error/404.html', status=500)


def csrf_failure(request, reason=''):
    return render(request, 'error/csrf.html')
