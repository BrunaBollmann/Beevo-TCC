from cadastro.views import *
from django.urls import path


urlpatterns = [
    path('', gerenciar_equipamento, name='gerenciamento'),
    path('editar/<int:id>', editar_equipamento, name='editar'),
    path('cadastrar/professor', cadastro_prof, name='cadastro_prof'),
    path('cadastrar/equipamento', cadastro_equipamento, name='cadastro_equipamento')
]
