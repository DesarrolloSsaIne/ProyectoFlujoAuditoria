from django.conf.urls import url, include
from apps.auditoria.views import AuditoriaList, AuditoriaDelete, AuditoriaCreate, AuditoriaUpdate, AuditoriaAuditoresList, \
    AuditoriaAuditorCreate, AuditoriaAuditorDelete, AuditoriaListDirector, AuditoriaListAreasDirector,AuditoriaDetalleDirector, AuditoriaAuditoresListDirector
from django.contrib.auth.decorators import login_required


urlpatterns = [


    url(r'crear/', login_required(AuditoriaCreate.as_view()), name='AuditoriaCrear'),
    url(r'listar/', login_required(AuditoriaList.as_view()), name='AuditoriaListar'),
    url('editar/(?P<pk>\d+)/$', login_required(AuditoriaUpdate.as_view()), name='AuditoriaEditar'),
    url('eliminar/(?P<pk>\d+)/$', login_required(AuditoriaDelete.as_view()), name='AuditoriaEliminar'),
    url('listaAuditores/(?P<pk>\d+)/$', login_required(AuditoriaAuditoresList.as_view()), name='AuditoriaAuditorListar'),
    url(r'crearAuditorAsignado/', login_required(AuditoriaAuditorCreate.as_view()), name='AuditoriaCrearAuditor'),
    url('eliminarAuditorAsignado/(?P<pk>\d+)/$', login_required(AuditoriaAuditorDelete.as_view()), name='AuditoriaAuditorEliminar'),

    url(r'listarDirector/(?P<pk>\d+)/(?P<estado>\d+)/$', login_required(AuditoriaListDirector.as_view()), name='AuditoriaListarDirector'),
    url(r'listarAreasDirector/', login_required(AuditoriaListAreasDirector.as_view()), name='AuditoriaListarAreasDirector'),
    url(r'detalleDirector/(?P<pk>\d+)/$', login_required(AuditoriaDetalleDirector.as_view()), name='AuditoriaDetalleDirector'),
    #url('editar/2/(?P<id_nivel>\d+)/$', SegundoNivelUpdate, name='SegundoNivelEditar'),

    url('listaAuditoresDirector/(?P<pk>\d+)/$', login_required(AuditoriaAuditoresListDirector.as_view()), name='AuditoriaAuditorListarDirector'),

]