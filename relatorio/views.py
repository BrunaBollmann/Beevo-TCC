from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from agendamento.models import *
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User

# Create your views here.


@login_required(login_url='/auth/login/')
def home(request):
    if request.user.is_staff:
        bd = Agendamento.objects.all()

        filter_day = request.GET.get('date')
        equipamento = request.GET.get('equipamento')
        responsavel = request.GET.get('responsavel')
        aula = request.GET.get('aula')
        sala = request.GET.get('sala')
        periodo = request.GET.get('periodo')

        if periodo is not None and periodo != 'None':
            bd = bd.filter(periodo_id=periodo)
        if sala is not None and sala != 'None':
            bd = bd.filter(sala_id=sala)
        if aula is not None and aula != 'None':
            bd = bd.filter(aula_id=aula)
        if responsavel is not None and responsavel != 'None':
            bd = bd.filter(responsavel_id=responsavel)
        if equipamento is not None and equipamento != 'None':
            bd = bd.filter(equipamento_id=equipamento)
        if not filter_day or filter_day == 'None' or filter_day is None:
            filter_day = 30

        bd = bd.filter(data__range=[timezone.localdate() - timedelta(int(filter_day)),
                                    timezone.localdate() + timedelta(int(filter_day))]).order_by('data')

        return render(request, 'relatorio/index.html', {'agendamento': bd,
                                                        'equipamento': Equipamento.objects.all().order_by('nome'),
                                                        'aula': Aula.objects.all(),
                                                        'sala': Sala.objects.all(),
                                                        'periodo': Periodo.objects.all(),
                                                        'periodo_id': periodo,
                                                        'aula_id': aula,
                                                        'sala_id': sala,
                                                        'equipamento_id': equipamento,
                                                        'dia': filter_day})
    else:
        return render(request, 'error/negado.html')
