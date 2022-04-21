from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from apps.bandeja_gestion.views import HallazgosList, ComprimisoList, CompromisoUpdate, ObservacionesCompromisosEnc, \
    ObservacionesCompromisosAuditor, ObservacionesCompromisosAuditado, ObservacionesCompromisosObservador, ObservacionesCompromisosAuditorDirector
from django.urls import path

urlpatterns = [

    url('listarHallazgoBandejaEnc/', login_required(HallazgosList.as_view()), name='listarHallazgoBandejaEnc'),
    url('listarCompromisoEnc/(?P<pk>\d+)/$', login_required(ComprimisoList.as_view()), name='listarCompromisoEnc'),
    url('CompromisoEditEstado/(?P<pk>\d+)/$', login_required(CompromisoUpdate.as_view()), name='CompromisoEditEstado'),
    path('ObservacionesCompromisosEnc/<int:pk>', ObservacionesCompromisosEnc,
         name="ObservacionesCompromisosEnc"),
    path('ObservacionesCompromisosAuditor/<int:pk>', ObservacionesCompromisosAuditor,
         name="ObservacionesCompromisosAuditor"),
    path('ObservacionesCompromisosAuditado/<int:pk>', ObservacionesCompromisosAuditado,
         name="ObservacionesCompromisosAuditado"),

    path('ObservacionesCompromisosObservador/<int:pk>', ObservacionesCompromisosObservador,
             name="ObservacionesCompromisosObservador"),

    path('ObservacionesCompromisosAuditorDirector/<int:pk>', ObservacionesCompromisosAuditorDirector,
         name="ObservacionesCompromisosAuditorDirector"),

    ]