from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.vista_auditorias.views import listarSegundoNivel, listarTercerNivel, listarCuartoNivel, AuditoriaListVista,HallazgosList, ComprimisoList


urlpatterns = [

url(r'listarNivelUsuario/', login_required(views.listarNivelUsuario), name='listarNivelUsuario'),
    path('listarSegundoNivel/<int:pk>', views.listarSegundoNivel, name='SegundoNivelVista'),
    path('listarTercerNivel/<int:pk>', views.listarTercerNivel, name='TercerNivelVista'),
    path('listarCuartoNivel/<int:pk>', views.listarCuartoNivel, name='CuartoNivelVista'),
    url('listarAuditoriasVista/(?P<pk>\d+)/(?P<orden>\d+)/$', login_required(AuditoriaListVista.as_view()), name='AuditoriaListarVista'),
    url('listarHallazgosVista/(?P<pk>\d+)/$', login_required(HallazgosList.as_view()), name='HallazgosListarVista'),
    url('listarCompromisoVista/(?P<pk>\d+)/$', login_required(ComprimisoList.as_view()), name='CompromisoListarVista'),
]