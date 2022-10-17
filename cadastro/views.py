from django.shortcuts import render, redirect
from cadastro.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page

# Create your views here.


@login_required(login_url='/auth/login/')
def gerenciar_equipamento(request):
    if request.user.is_staff:
        equipamentos = Equipamento.objects.all().order_by('nome')
        return render(request, 'gerenciar/index.html', {'equip': equipamentos})
    else:
        return render(request, 'error/negado.html')


@login_required(login_url='/auth/login/')
def cadastro_prof(request):
    if request.user.is_staff:
        if request.method == 'GET':
            form = CadastrarProf
            return render(request, 'gerenciar/professor.html', {'form': form, })
        else:
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')
            username = request.POST.get('apelido')
            matricula = request.POST.get('matricula')
            senha = request.POST.get('senha')
            confirm = request.POST.get('senha_confirm')
            staff = request.POST.get('staff')

            user = User.objects.filter(email=matricula).first()
            user2 = User.objects.filter(username=username).first()

            try:
                int(matricula)
            except ValueError:
                return render(request, 'gerenciar/professor.html', {'form': CadastrarProf,
                                                                    'error': 3})

            if user or user2:
                return render(request, 'gerenciar/professor.html', {'form': CadastrarProf,
                                                                    'error': 1})

            if senha == confirm:
                user = User.objects.create_user(first_name=nome, last_name=sobrenome, email=matricula,
                                                password=senha, is_staff=staff, username=username)
                user.save()
                return render(request, 'gerenciar/professor.html', {'sucess': 1,
                                                                    'nome_prof': nome,
                                                                    'form': CadastrarProf})
            else:
                return render(request, 'gerenciar/professor.html', {'form': CadastrarProf,
                                                                    'error': 2})

    else:
        return render(request, 'error/negado.html')


@login_required(login_url='/auth/login/')
def cadastro_equipamento(request):
    if request.user.is_staff:
        if request.method == 'GET':
            form = CadastrarEquip
            return render(request, 'gerenciar/equipamento.html', {'form': form})
        else:
            form = CadastrarEquip(request.POST)
            if form.is_valid():
                nome = request.POST.get('nome')
                bd = Equipamento.objects.filter(nome=nome).first()
                if bd:
                    return render(request, 'gerenciar/equipamento.html', {'error': 1,
                                                                          'nome_equip': nome,
                                                                          'form': form})
                novo = Equipamento.objects.create(nome=nome, ativo=1)
                return render(request, 'gerenciar/equipamento.html', {'sucess': 1,
                                                                      'nome_equip': nome,
                                                                      'form': form})
    else:
        return render(request, 'error/negado.html')


@login_required(login_url='/auth/login/')
def editar_equipamento(request, id):
    if request.method == 'GET':
        equip = Equipamento.objects.get(id=id)
        form = CadastrarEquip(instance=equip)
    else:
        equip = Equipamento.objects.get(id=id)
        form = CadastrarEquip(request.POST, instance=equip)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'error/negado.html')
    return render(request, 'gerenciar/editar_equipamento.html', {'form': form})


