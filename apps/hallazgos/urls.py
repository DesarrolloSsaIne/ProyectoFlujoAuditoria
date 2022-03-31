from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.hallazgos.views import HallazgosList, hallazgoCreate, hallazgoDelete, hallazgoUpdate, hallazgoUpdateEstado,download_file,AuditoriasListAuditado

urlpatterns = [

    url('listarHallazgos/(?P<pk>\d+)/$', login_required(HallazgosList.as_view()), name='HallazgosListar'),
    url('listarAuditoriasAuditado/', login_required(AuditoriasListAuditado.as_view()), name='AuditoriasListarAuditado'),
    url(r'HallazgoCrear/', login_required(hallazgoCreate.as_view()), name='HallazgoCrear'),
    url('hallazgoEliminar/(?P<pk>\d+)/$', login_required(hallazgoDelete.as_view()), name='hallazgoEliminar'),
    url('hallazgoEditar/(?P<pk>\d+)/$', login_required(hallazgoUpdate.as_view()), name='hallazgoEditar'),
    url(r'^hallazgoUpdateEstado/', hallazgoUpdateEstado, name='hallazgoUpdateEstado'),
    url(r'^download/(?P<path>.*)$', download_file, name='donwload'),


    ]