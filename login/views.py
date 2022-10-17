from django.shortcuts import render, redirect
from login.forms import *
from django.contrib.auth import authenticate, login, logout
from agendamento.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def logar(request):
    if request.method == 'GET':
        return render(request, 'login/signin.html', {'form': Login})
    else:
        try:
            matricula = request.POST.get('matricula')
            senha = request.POST.get('senha')

            username = User.objects.get(email=matricula)
            username = username.username
            user = authenticate(username=username, password=senha)

            if user:
                login(request, user)

                return redirect('/')
            else:
                return render(request, 'login/signin.html', {'error': 1,
                                                             'form': Login})
        except:
            return render(request, 'login/signin.html', {'error': 1,
                                                         'form': Login})


@login_required(login_url='/auth/login/')
def sair(request):
    logout(request)
    return redirect('/auth/login')
