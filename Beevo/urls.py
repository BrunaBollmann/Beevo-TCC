from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('agendamento.urls')),
    path('auth/', include('login.urls')),
    path('gerenciar/', include('cadastro.urls')),
    path('sobre/', include('sobre.urls')),
    path('relatorio/', include('relatorio.urls')),
]

handler404 = 'agendamento.views.page_not_found_view'

# handler500 = 'agendamento.views.handler500'
