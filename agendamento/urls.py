from agendamento.views import *
from django.urls import path


urlpatterns = [
    path('', index),
    path('agendamento<int:id>/', agendamento, name='agendar'),
    path('excluir<int:id>/', excluir, name='excluir'),
    path('instrucoes/', instrucao, name='instrucao'),
]

