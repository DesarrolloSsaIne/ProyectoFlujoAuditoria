from django.urls import path
from . import views
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # path('listarPrimerNivel/', views.listarPrimerNivel, name='PrimerNivel'),
    url(r'listarPrimerNivel/', login_required(views.listarPrimerNivel), name='PrimerNivel'),
    path('listarSegundoNivel/<int:pk>', views.listarSegundoNivel, name='SegundoNivel'),
    path('listarTercerNivel/<int:pk>', views.listarTercerNivel, name='TercerNivel'),
    path('listarCuartoNivel/<int:pk>', views.listarCuartoNivel, name='CuartoNivel'),


]