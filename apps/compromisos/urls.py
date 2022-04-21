from django.conf.urls import url
from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.compromisos.views import HallazgosList, ComprimisoList, CompromisoCreate, CompromisoDelete, \
    CompromisoResponsableUpdate, CompromisoUpdate,\
    EnviaCompromiso, hallazgoDetalleCompomiso, ComprimisoAuditorList, CompromisoValidarAuditor, \
    update_compromiso_rechaza, update_compromiso_acepta,HallazgoCreateEncargadoGestion, CompromisoDevolverEG,\
    CompromisoCreateEg,CompromisoUpdateEg,CompromisoDeleteEg,CompromisoResponsableUpdateEg, export_users_xls_auditoria_auditor, \
    export_users_xls_auditoria_auditado, CompromisoUpdateAuditor, ComprimisoAuditorListDirector




urlpatterns = [
    url('listarHallazgoBandeja/(?P<pk>\d+)/$', login_required(HallazgosList.as_view()), name='listarHallazgoBandeja'),
    url('listarCompromiso/(?P<pk>\d+)/$', login_required(ComprimisoList.as_view()), name='CompromisoListar'),
    url(r'CrompromisoCrear/', login_required(CompromisoCreate.as_view()), name='CompromisoCrear'),
    url('CrompromisoEliminar/(?P<pk>\d+)/$', login_required(CompromisoDelete.as_view()), name='CrompromisoDelete'),
    url('compromisoEditar/(?P<pk>\d+)/$', login_required(CompromisoUpdate.as_view()), name='CompromisoEdit'),
    url('compromisoEditarAuditor/(?P<pk>\d+)/$', login_required(CompromisoUpdateAuditor.as_view()), name='CompromisoEditAuditor'),
    url('CompromisoResponsableEditar/(?P<pk>\d+)/$', login_required(CompromisoResponsableUpdate.as_view()), name='CompromisoResponsableEdit'),
    url('EnviarCompromiso/(?P<pk>\d+)/$', login_required(EnviaCompromiso.as_view()), name='EnviarCompromiso'),
    url('hallazgoDetalleCompromiso/(?P<pk>\d+)/$', login_required(hallazgoDetalleCompomiso.as_view()), name='hallazgoDetalleCompromiso'),
    url('hallazgoDetalleCompromisoAuditor/(?P<pk>\d+)/$', login_required(ComprimisoAuditorList.as_view()), name='CompromisoAuditorList'),
    url('compromisoValidarAuditor/(?P<pk>\d+)/$', login_required(CompromisoValidarAuditor.as_view()), name='CompromisoValidaAuditor'),
    url(r'compromiso_rechaza_auditor/', update_compromiso_rechaza, name='compromiso_rechaza_auditor'),
    url(r'compromiso_acepta_auditor/', update_compromiso_acepta, name='compromiso_acepta_auditor'),
    url(r'hallazgoAsignaEncargadoGestion/(?P<pk>\d+)/$', login_required(HallazgoCreateEncargadoGestion.as_view()), name='HallazgoAsignaEg'),
    url(r'compromisoDevuelveEG/(?P<pk>\d+)/$', login_required(CompromisoDevolverEG.as_view()), name='CompromisoDevuelveEG'),


    url(r'CrompromisoCrearEg/', login_required(CompromisoCreateEg.as_view()), name='CompromisoCrearEg'),
    url('compromisoEditarEg/(?P<pk>\d+)/$', login_required(CompromisoUpdateEg.as_view()), name='CompromisoEditEg'),
    url('CrompromisoEliminarEg/(?P<pk>\d+)/$', login_required(CompromisoDeleteEg.as_view()), name='CrompromisoDeleteEg'),
    url('CompromisoResponsableEditarEg/(?P<pk>\d+)/$', login_required(CompromisoResponsableUpdateEg.as_view()), name='CompromisoResponsableEditEg'),

    path(r'ExportarReporteAuditoriaAuditor/<int:pk>', export_users_xls_auditoria_auditor, name='exporta_reporte_auditoria_auditor_xls'),
    path(r'ExportarReporteAuditoriaAuditado/<int:pk>', export_users_xls_auditoria_auditado, name='exporta_reporte_auditoria_auditado_xls'),

    url('hallazgoDetalleCompromisoAuditorDirector/(?P<pk>\d+)/$', login_required(ComprimisoAuditorListDirector.as_view()), name='CompromisoAuditorListDirector'),
    ]