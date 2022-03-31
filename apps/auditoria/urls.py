from django.conf.urls import url, include
from apps.auditoria.views import AuditoriaList, AuditoriaDelete, AuditoriaCreate, AuditoriaUpdate, AuditoriaAuditoresList, AuditoriaAuditorCreate, AuditoriaAuditorDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [


    url(r'crear/', login_required(AuditoriaCreate.as_view()), name='AuditoriaCrear'),
    url(r'listar/', login_required(AuditoriaList.as_view()), name='AuditoriaListar'),
    url('editar/(?P<pk>\d+)/$', login_required(AuditoriaUpdate.as_view()), name='AuditoriaEditar'),
    url('eliminar/(?P<pk>\d+)/$', login_required(AuditoriaDelete.as_view()), name='AuditoriaEliminar'),
    url('listaAuditores/(?P<pk>\d+)/$', login_required(AuditoriaAuditoresList.as_view()), name='AuditoriaAuditorListar'),
    url(r'crearAuditorAsignado/', login_required(AuditoriaAuditorCreate.as_view()), name='AuditoriaCrearAuditor'),
    url('eliminarAuditorAsignado/(?P<pk>\d+)/$', login_required(AuditoriaAuditorDelete.as_view()), name='AuditoriaAuditorEliminar'),

    #url('editar/2/(?P<id_nivel>\d+)/$', SegundoNivelUpdate, name='SegundoNivelEditar'),

]