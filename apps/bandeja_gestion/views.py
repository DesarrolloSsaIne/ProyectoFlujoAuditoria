from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
from datetime import datetime
from apps.compromisos.models import Ges_Compromisos, Ges_Observaciones_Compromiso_Enc
from apps.hallazgos.models import Ges_Hallazgo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from apps.compromisos.forms import CompromisoEditFormEstado
from django.contrib import messages

from django.core.mail import EmailMessage

from apps.jefaturas.models import Ges_Jefatura


class HallazgosList(ListView):
    model = Ges_Hallazgo
    template_name = 'bandeja_gestion/bandeja_gestion_hallazgos_list.html'

    def get_context_data(self,  **kwargs):
        context = super(HallazgosList, self).get_context_data(**kwargs)

        id_usuario = self.request.user.id
        lista_hallazgos = Ges_Hallazgo.objects.filter(Q(enc_gestion_id = id_usuario ) & Q (id_estadoshallazgo_id__in =[1,2,3,4]))

        context['object_list'] = lista_hallazgos


        #self.request.session['pk_auditoria'] = self.kwargs['pk']
        return context

class ComprimisoList(ListView):
    model = Ges_Compromisos
    template_name = 'bandeja_gestion/enc_gestion_compromisos_list.html'

    def get_context_data(self,  **kwargs):
        context = super(ComprimisoList, self).get_context_data(**kwargs)

        lista_compromisos = Ges_Compromisos.objects.filter(hallazgo_id=self.kwargs['pk'])
        #auditoria = Ges_auditoria.objects.get(id=self.kwargs['pk'])
        hallazgo =  Ges_Hallazgo.objects.get(id=self.kwargs['pk'])
        context['object_list'] = lista_compromisos
        context['auditoria'] ={ 'nombre' : str(hallazgo.id_auditoria.descripcion_auditoria), 'numero' : str(hallazgo.id_auditoria.cod_auditoria) }

        self.request.session['pk_hallazgo'] = self.kwargs['pk']
        return context

def ObservacionesCompromisosEnc(request, pk):
    id_usuario_actual = request.user.id

    id_estado_compromiso= Ges_Compromisos.objects.filter(id=pk)

    Observaciones_Compromiso = Ges_Observaciones_Compromiso_Enc.objects.filter(compromiso_observacion_id=pk)
    t = loader.get_template('bandeja_gestion/modal_observaciones.html')
    c = {'ObjectList': Observaciones_Compromiso, 'pk': pk, 'estado_compromiso': id_estado_compromiso}


    if request.method == "POST":
        #print(request.POST)
        data = {}
        observacion = request.POST.get('observacion')

        data['observacion'] = observacion
        data['id_compromiso'] = pk
        data['usuario'] = request.user.get_full_name()
        ahora = datetime.now()
        fecha = ahora.strftime("%d" + " de " + "%B" + " de " + "%Y" + " a las " + "%H:%M")
        data['fecha'] = fecha

        Ges_Observaciones_Compromiso_Enc.objects.create(
            descripcion_Observacion=observacion, fecha_observacion=ahora, visto=0, usuario_observacion_id=id_usuario_actual, compromiso_observacion_id=pk,
        )
        return JsonResponse(data)

    return HttpResponse(t.render(c, request ), content_type='text/html; charset=utf-8', )


def ObservacionesCompromisosAuditado(request, pk):
    id_usuario_actual = request.user.id

    id_estado_compromiso= Ges_Compromisos.objects.filter(id=pk)

    Observaciones_Compromiso = Ges_Observaciones_Compromiso_Enc.objects.filter(compromiso_observacion_id=pk)
    t = loader.get_template('bandeja_gestion/modal_observaciones_auditado.html')
    c = {'ObjectList': Observaciones_Compromiso, 'pk': pk, 'estado_compromiso': id_estado_compromiso}


    if request.method == "POST":
        #print(request.POST)
        data = {}
        observacion = request.POST.get('observacion')

        data['observacion'] = observacion
        data['id_compromiso'] = pk
        data['usuario'] = request.user.get_full_name()
        ahora = datetime.now()
        fecha = ahora.strftime("%d" + " de " + "%B" + " de " + "%Y" + " a las " + "%H:%M")
        data['fecha'] = fecha

        Ges_Observaciones_Compromiso_Enc.objects.create(
            descripcion_Observacion=observacion, fecha_observacion=ahora, visto=0, usuario_observacion_id=id_usuario_actual, compromiso_observacion_id=pk,
        )
        return JsonResponse(data)

    return HttpResponse(t.render(c, request ), content_type='text/html; charset=utf-8', )


def ObservacionesCompromisosObservador(request, pk):
    id_usuario_actual = request.user.id

    id_estado_compromiso= Ges_Compromisos.objects.filter(id=pk)

    Observaciones_Compromiso = Ges_Observaciones_Compromiso_Enc.objects.filter(compromiso_observacion_id=pk)
    t = loader.get_template('bandeja_gestion/modal_observaciones_observador.html')
    c = {'ObjectList': Observaciones_Compromiso, 'pk': pk, 'estado_compromiso': id_estado_compromiso}


    if request.method == "POST":
        #print(request.POST)
        data = {}
        observacion = request.POST.get('observacion')

        data['observacion'] = observacion
        data['id_compromiso'] = pk
        data['usuario'] = request.user.get_full_name()
        ahora = datetime.now()
        fecha = ahora.strftime("%d" + " de " + "%B" + " de " + "%Y" + " a las " + "%H:%M")
        data['fecha'] = fecha

        Ges_Observaciones_Compromiso_Enc.objects.create(
            descripcion_Observacion=observacion, fecha_observacion=ahora, visto=0, usuario_observacion_id=id_usuario_actual, compromiso_observacion_id=pk,
        )
        return JsonResponse(data)

    return HttpResponse(t.render(c, request ), content_type='text/html; charset=utf-8', )



def ObservacionesCompromisosAuditor(request, pk):
    id_usuario_actual = request.user.id

    id_estado_compromiso= Ges_Compromisos.objects.filter(id=pk)

    Observaciones_Compromiso = Ges_Observaciones_Compromiso_Enc.objects.filter(compromiso_observacion_id=pk)
    t = loader.get_template('bandeja_gestion/modal_observaciones_auditor.html')
    c = {'ObjectList': Observaciones_Compromiso, 'pk': pk, 'estado_compromiso': id_estado_compromiso}


    if request.method == "POST":
        #print(request.POST)
        data = {}
        observacion = request.POST.get('observacion')

        data['observacion'] = observacion
        data['id_compromiso'] = pk
        data['usuario'] = request.user.get_full_name()
        ahora = datetime.now()
        fecha = ahora.strftime("%d" + " de " + "%B" + " de " + "%Y" + " a las " + "%H:%M")
        data['fecha'] = fecha

        Ges_Observaciones_Compromiso_Enc.objects.create(
            descripcion_Observacion=observacion, fecha_observacion=ahora, visto=0, usuario_observacion_id=id_usuario_actual, compromiso_observacion_id=pk,
        )
        return JsonResponse(data)

    return HttpResponse(t.render(c, request ), content_type='text/html; charset=utf-8', )


def ObservacionesCompromisosAuditorDirector(request, pk):
    id_usuario_actual = request.user.id

    id_estado_compromiso= Ges_Compromisos.objects.filter(id=pk)

    Observaciones_Compromiso = Ges_Observaciones_Compromiso_Enc.objects.filter(compromiso_observacion_id=pk)
    t = loader.get_template('bandeja_gestion/modal_observaciones_auditor_director.html')
    c = {'ObjectList': Observaciones_Compromiso, 'pk': pk, 'estado_compromiso': id_estado_compromiso}


    if request.method == "POST":
        #print(request.POST)
        data = {}
        observacion = request.POST.get('observacion')

        data['observacion'] = observacion
        data['id_compromiso'] = pk
        data['usuario'] = request.user.get_full_name()
        ahora = datetime.now()
        fecha = ahora.strftime("%d" + " de " + "%B" + " de " + "%Y" + " a las " + "%H:%M")
        data['fecha'] = fecha

        Ges_Observaciones_Compromiso_Enc.objects.create(
            descripcion_Observacion=observacion, fecha_observacion=ahora, visto=0, usuario_observacion_id=id_usuario_actual, compromiso_observacion_id=pk,
        )
        return JsonResponse(data)

    return HttpResponse(t.render(c, request ), content_type='text/html; charset=utf-8', )

class CompromisoUpdate(SuccessMessageMixin, UpdateView ):
    model = Ges_Compromisos
    form_class = CompromisoEditFormEstado
    template_name = 'bandeja_gestion/compromiso_form_update_state.html'
    def get_context_data(self,  **kwargs):
        context = super(CompromisoUpdate, self).get_context_data(**kwargs)

        try:
            id_compromiso = Ges_Compromisos.objects.get(id=self.kwargs['pk'])
        except Ges_Hallazgo.DoesNotExist:
            return None
        context = {"tiene_responsable": id_compromiso.responsable_hallazgo_id}

        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object
        id = kwargs['pk']
        id_compromiso = self.model.objects.get(id=id)
        hallazgo = Ges_Hallazgo.objects.get(id=id_compromiso.hallazgo_id_id)
        auditado = Ges_Jefatura.objects.get(id=hallazgo.jefatura_id_id)
        form = self.form_class(request.POST, instance=id_compromiso)


        if form.is_valid():
            form.instance.estado_compromiso_id = '5'
            form.save()
            hallazgoUpdateEstado(hallazgo.id, 4)
            respuesta_mail = EnviarCorreoInicioSeguimiento(auditado.id_user.email, hallazgo.id_auditoria.cod_auditoria,
                                          hallazgo.id_auditoria.descripcion_auditoria)
            request.session['message_class'] = "alert alert-success"
            if respuesta_mail == False:
                request.session['message_class'] = "alert alert-warning"
                respuesta_mail = 'Ops! ocurrio un error al enviar el correo de notificación'
            messages.success(self.request, "El compromiso fue enviado a validación del Responsable de Área! ")
            return HttpResponseRedirect('/bandeja_gestion/listarCompromisoEnc/'+ str(self.request.session['pk_hallazgo']))
        else:
            request.session['message_class'] = "alert alert-danger"
            messages.error(self.request, "Error interno: No se ha actualizado el registro. Comuníquese con el administrador.")
            return HttpResponseRedirect('/bandeja_gestion/listarCompromisoEnc/' + str(self.request.session['pk_hallazgo']))

def hallazgoUpdateEstado(id_hallazgo, id_estado):

    hallazgo = Ges_Hallazgo.objects.get(id =id_hallazgo )
    hallazgo.id_estadoshallazgo_id = int(id_estado)
    hallazgo.save()

    return None

def EnviarCorreoInicioSeguimiento(auditores_emails, cod_auditoria, descripcion_auditoria):

    # ahora = datetime.now()
    # fecha = ahora.strftime("%d" + "/" + "%m" + "/" + "%Y" + " a las " + "%H:%M")
    cod_auditoria = str(cod_auditoria)
    descripcion_auditoria = str(descripcion_auditoria)
    idcorreoJefatura=[auditores_emails]

    subject = 'Revisión Compromiso de Auditoría'
    messageHtml = '<b>Estimado/a</b>: <br><br> En el marco de la auditoria en curso <b>'+ cod_auditoria +'</b> <b>'+ descripcion_auditoria +'</b>, se requiere su ingreso al Sistema de Auditoria Institucional, para proceder a la revisión del/los compromisos ingresados por el Encargado de Gestionar Compromiso.. <b> <br> El link de acceso es:  <a href="http://seguimientoauditoria.ine.cl:8008/accounts/login/"> Sistema Auditoría'
    email = EmailMessage(subject, messageHtml ,to=idcorreoJefatura)
    email.content_subtype='html'
    try:
        email.send()
        return True
    except:
        return False