
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'accounts/', include('apps.registration.urls')),
    path(r'dashboard/', include('apps.dashboard.urls')),
    path(r'estructura_jerarquica/', include('apps.estructura_jerarquica.urls')),
    path(r'jefaturas/', include('apps.jefaturas.urls')),
    path(r'auditorias/', include('apps.auditoria.urls')),
    path(r'hallazgos/', include('apps.hallazgos.urls')),
    path(r'compromisos/', include('apps.compromisos.urls')),
    path(r'bandeja_gestion/', include('apps.bandeja_gestion.urls')),
    path(r'vista_auditorias/', include('apps.vista_auditorias.urls')),

]

