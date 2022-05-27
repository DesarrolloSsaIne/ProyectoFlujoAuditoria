import mimetypes
import os
from django.conf import settings
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models.deletion import ProtectedError
from apps.compromisos.models import Ges_Compromisos
from apps.estados_hallazgo.models import Glo_EstadosHallazgo
from apps.hallazgos.models import Ges_Hallazgo
from apps.auditoria.models import Ges_auditoria
from apps.jefaturas.models import Ges_Jefatura
from apps.jefaturas.models import Ges_Jefatura
# Create your views here.
from apps.hallazgos.forms import HallazgoAddForm, HallazgoUpdateForm,HallazgoDetalleDirectorForm
from django.http import HttpResponseRedirect, JsonResponse
from django.core.mail import EmailMessage,send_mass_mail
from django.db.models import Subquery, OuterRef, Count
from django.db.models import Q
from datetime import datetime
IMAGE_FILE_TYPES = ['bat', 'exe', 'rar' ]
SIZE = 10485760

class AuditoriasListAuditado(ListView):
    model = Ges_auditoria
    template_name = 'hallazgos/auditorias_list_auditado.html'

    def get_context_data(self,  **kwargs):
        context = super(AuditoriasListAuditado, self).get_context_data(**kwargs)
        id_usuario = self.request.user.id
        id_jefatura= Ges_Jefatura.objects.get(id_user_id=id_usuario)
        lista_auditorias = Ges_auditoria.objects.filter(jefatura_id_id=id_jefatura.id)


        count_hallazgos = Ges_Hallazgo.objects.values('id_auditoria').filter(Q(id_auditoria=OuterRef('pk')) &
                                                                             Q(id_estadoshallazgo_id__in =[ 1,2,3,4,5])
            ).annotate(
            count_id_auditoria=Count('id_auditoria'))


        lista_auditorias = Ges_auditoria.objects.filter(jefatura_id_id=id_jefatura.id).annotate(
        count_hallazgos=Subquery(count_hallazgos.values('count_id_auditoria')))









       # context['count_hallazgos'] = {'cantidad':count_hallazgos}
        context['object_list'] = lista_auditorias
       # context['auditoria'] ={ 'nombre' : str(auditoria.descripcion_auditoria), 'numero' : str(auditoria.cod_auditoria) }

       # self.request.session['pk_auditoria'] = self.kwargs['pk']
        return context


class HallazgosList(ListView):
    model = Ges_Hallazgo
    template_name = 'hallazgos/hallazgos_list.html'

    def get_context_data(self,  **kwargs):
        context = super(HallazgosList, self).get_context_data(**kwargs)

        lista_hallazgos = Ges_Hallazgo.objects.filter(id_auditoria_id=self.kwargs['pk'])
        auditoria = Ges_auditoria.objects.get(id=self.kwargs['pk'])
        context['object_list'] = lista_hallazgos
        context['auditoria'] ={ 'nombre' : str(auditoria.descripcion_auditoria), 'numero' : str(auditoria.cod_auditoria) }

        self.request.session['pk_auditoria'] = self.kwargs['pk']
        return context


class HallazgosListDirector(ListView):
    model = Ges_Hallazgo
    template_name = 'hallazgos/hallazgos_list_director.html'

    def get_context_data(self,  **kwargs):
        context = super(HallazgosListDirector, self).get_context_data(**kwargs)

        count_abiertas = Ges_Compromisos.objects.values('hallazgo_id').filter(
            hallazgo_id=OuterRef('pk')).annotate(
            count_compomisos=Count('id'))

        lista_hallazgos = Ges_Hallazgo.objects.filter(id_auditoria_id=self.kwargs['pk']).annotate(
            count_compromisos_hallazgo=Subquery(count_abiertas.values('count_compomisos')))

        #lista_hallazgos = Ges_Hallazgo.objects.filter(id_auditoria_id=self.kwargs['pk'])

        auditoria = Ges_auditoria.objects.get(id=self.kwargs['pk'])
        context['object_list'] = lista_hallazgos
        context['auditoria'] ={ 'nombre' : str(auditoria.descripcion_auditoria), 'numero' : str(auditoria.cod_auditoria) }

        self.request.session['pk_auditoria'] = self.kwargs['pk']
        return context


class hallazgoDetalleDirector(SuccessMessageMixin, UpdateView ):
    model = Ges_Hallazgo
    form_class = HallazgoDetalleDirectorForm
    template_name = 'hallazgos/hallazgo_detalle_director.html'

    def get_context_data(self,  **kwargs):
        context = super(hallazgoDetalleDirector, self).get_context_data(**kwargs)

        try:
            hallazgo = Ges_Hallazgo.objects.get(id=self.kwargs['pk'])
        except Ges_Hallazgo.DoesNotExist:
            return None

        try:
            hallazgo = Ges_Hallazgo.objects.get(id=self.kwargs['pk'])
        except Ges_Hallazgo.DoesNotExist:
            return None

        if hallazgo.document:
            documento= hallazgo.document
        else:
            documento='0'

        context['hallazgo'] = {'id': hallazgo.id,'document': documento,}

        return context


# class hallazgoDetalleDirector(SuccessMessageMixin, DetailView ):
#     model = Ges_Hallazgo
#     template_name = 'hallazgos/hallazgo_detalle_director.html'
#
#     def get_context_data(self,  **kwargs):
#         context = super(hallazgoDetalleDirector, self).get_context_data(**kwargs)
#
#         try:
#             hallazgo = Ges_Hallazgo.objects.get(id=self.kwargs['pk'])
#         except Ges_Hallazgo.DoesNotExist:
#             return None
#
#         try:
#             hallazgo = Ges_Hallazgo.objects.get(id=self.kwargs['pk'])
#         except Ges_Hallazgo.DoesNotExist:
#             return None
#
#         if hallazgo.document:
#             documento= hallazgo.document
#         else:
#             documento='0'
#
#         context['hallazgo'] = {'id': hallazgo.id,'document': documento,}
#
#         return context



class hallazgoCreate(SuccessMessageMixin, CreateView ):
    form_class = HallazgoAddForm
    template_name = 'hallazgos/hallazgo_form.html'


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        #form = self.get_form(form_class)
        form = HallazgoAddForm(request.POST, request.FILES)

        print(form.errors.as_json())
        if form.is_valid():
            files = form.files.__len__()
            if files > 0:
                filetype = str(form.instance.document.name)
                filetype = filetype.split('.')[-1]
                size = str(form.instance.document.size)
            form.instance.id_auditoria_id = self.request.session['pk_auditoria']
            if files > 0:
                if filetype not in IMAGE_FILE_TYPES:
                    form.save()
                    request.session['message_class'] = "alert alert-success"
                    messages.success(self.request, "Los datos fueron creados correctamente!")
                    return HttpResponseRedirect('/hallazgos/listarHallazgos/'+ str(self.request.session['pk_auditoria']))
                else:
                    request.session['message_class'] = "alert alert-warning"
                    messages.error(self.request,
                                  "El tipo de archivo no esta permitido por el sistema, intente en otro formato.")
                    return HttpResponseRedirect(
                        '/hallazgos/listarHallazgos/' + str(self.request.session['pk_auditoria']))
            else:
                form.save()
                request.session['message_class'] = "alert alert-success"
                messages.success(self.request, "Los datos fueron creados correctamente!")
                return HttpResponseRedirect('/hallazgos/listarHallazgos/' + str(self.request.session['pk_auditoria']))
        else:
            request.session['message_class'] = "alert alert-danger"
            messages.error(self.request, "Error interno: No se ha creado el registro. Comuníquese con el administrador.")
            return HttpResponseRedirect('/hallazgos/listarHallazgos/'+ str(self.request.session['pk_auditoria']))

class hallazgoDelete(SuccessMessageMixin, DeleteView ):
    model = Ges_Hallazgo
    template_name = 'hallazgos/hallazgo_delete.html'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            obj.delete()


            request.session['message_class'] = "alert alert-success"
            messages.success(self.request, "El registro fue eliminado correctamente!")
            return HttpResponseRedirect('/hallazgos/listarHallazgos/'+ str(self.request.session['pk_auditoria']))

        except ProtectedError as e:
            request.session['message_class'] = "alert alert-danger"
            messages.error(request, "Error de integridad: No se puede eliminar esta auditoría porque tiene registros asociados.")
            return HttpResponseRedirect('/hallazgos/listarHallazgos/'+ str(self.request.session['pk_auditoria']))

        except Exception  as e:
            request.session['message_class'] = "alert alert-danger"
            messages.error(request, "Error interno: No se ha eliminado el registro. Comuníquese con el administrador.")
            return HttpResponseRedirect('/hallazgos/listarHallazgos/'+ str(self.request.session['pk_auditoria']))


class hallazgoUpdate(SuccessMessageMixin, UpdateView ):
    model = Ges_Hallazgo
    form_class = HallazgoUpdateForm
    template_name = 'hallazgos/hallazgo_form_update.html'

    def get_context_data(self,  **kwargs):
        context = super(hallazgoUpdate, self).get_context_data(**kwargs)

        try:
            hallazgo = Ges_Hallazgo.objects.get(id=self.kwargs['pk'])
        except Ges_Hallazgo.DoesNotExist:
            return None

        try:
            hallazgo = Ges_Hallazgo.objects.get(id=self.kwargs['pk'])
        except Ges_Hallazgo.DoesNotExist:
            return None

        context['hallazgo'] = {'id': hallazgo.id, 'estado_hallazgo':hallazgo.id_estadoshallazgo_id}

        return context

    def post(self, request, *args, **kwargs):

        self.object = self.get_object
        id = kwargs['pk']
        id_hallazgo = self.model.objects.get(id=id)
        form = self.form_class(request.POST,  request.FILES ,instance=id_hallazgo)

        if form.is_valid():
            form.save()
            request.session['message_class'] = "alert alert-success"
            messages.success(self.request, "Los datos fueron actualizados correctamente!" )
            return HttpResponseRedirect('/hallazgos/listarHallazgos/'+ str(self.request.session['pk_auditoria']))
        else:
            request.session['message_class'] = "alert alert-danger"
            messages.error(self.request, "Error interno: No se ha actualizado el registro. Comuníquese con el administrador.")
            return HttpResponseRedirect('/hallazgos/listarHallazgos/'+ str(self.request.session['pk_auditoria']))



def hallazgoUpdateEstado(request):
    id_hallazgo = request.POST.get('id_hallazgo')
    response_data = {}
    if request.POST.get('action') == 'post':
        #Valores a recibir del form
        id_hallazgo = request.POST.get('id_hallazgo')
        estado_hallazgo = request.POST.get('estado_hallazgo')

        #buscar el modelo a actualizar
        hallazgo = Ges_Hallazgo.objects.get(id=id_hallazgo)
        hallazgo.id_estadoshallazgo_id = int(estado_hallazgo)
        auditado = Ges_Jefatura.objects.get(id = hallazgo.jefatura_id_id)


        id_estadohallazgo = Glo_EstadosHallazgo.objects.get(id=1)


        # hallazgo.save()

        try:

            Ges_Hallazgo.objects.filter(id=id_hallazgo).update(id_estadoshallazgo=id_estadohallazgo.id)


        except:
          response_data['error'] = '3'



        try:

            EnviarCorreoInicioHallazgo(auditado.id_user.email, hallazgo.id_auditoria.cod_auditoria,
                                         hallazgo.id_auditoria.descripcion_auditoria)

            response_data['error'] = '1'



        except:
            response_data['error'] = '2'




          # if response_mail == False:
          #
          #     response_data['error'] = '2'
          # response_data['error'] = '1'


        return JsonResponse(response_data)




    return render(request, '/hallazgos/listarHallazgos/' + str(id_hallazgo), {'messages': 'true'})



def EnviarCorreoInicioHallazgo(auditores_emails, cod_auditoria, descripcion_auditoria):
    # ahora = datetime.now()
    # fecha = ahora.strftime("%d" + "/" + "%m" + "/" + "%Y" + " a las " + "%H:%M")
    # cod_auditoria = str(cod_auditoria)
    # descripcion_auditoria = str(descripcion_auditoria)
    # idcorreoJefatura=[auditores_emails]
    #
    # subject = 'Asignación Hallazgo de Auditoría'
    # messageHtml = '<b>Estimado/a Usuario/a</b>: <br><br> En el marco de la auditoria en curso <b>'+ cod_auditoria +'</b> relacionada a <b>'+ descripcion_auditoria +'</b> realizada por el Depto de Auditoria Institucional, se requiere su ingreso al Sistema de Auditoria Institucional, para proceder al ingreso de sus compromisos de acuerdo a cada hallazgo levantado.  El plazo para ingresar la información requerida, es de 5 días hábiles a partir de la recepción de éste correo. <b> <br> El link de acceso es:  <a href="http://10.91.160.63:81/accounts/login/"> Sistema Auditoría'
    # email = EmailMessage(subject, messageHtml,from_email=settings.EMAIL_HOST_USER  ,to=idcorreoJefatura)
    # email.content_subtype='html'
    # try:
    #     email.send()
    #     return True
    # except:
    #     return False

    # ahora = datetime.now()
    # fecha = ahora.strftime("%d" + "/" + "%m" + "/" + "%Y" + " a las " + "%H:%M")
    cod_auditoria = str(cod_auditoria)
    idcorreoJefatura=[auditores_emails]

    subject = 'Asignación Hallazgo de Auditoría'
    messageHtml = '<b>Estimado/a Usuario/a</b>: <br><br> En el marco de la auditoria en curso <b>'+ cod_auditoria +'</b> relacionada a <b>'+ descripcion_auditoria +'</b> realizada por el Depto de Auditoria Institucional, se requiere su ingreso al Sistema de Auditoria Institucional, para proceder al ingreso de sus compromisos de acuerdo a cada hallazgo levantado.  El plazo para ingresar la información requerida, es de 5 días hábiles a partir de la recepción de éste correo. <b> <br> El link de acceso es:  <a href="http://seguimientoauditoria.ine.cl:8008/accounts/login/"> Sistema Auditoría'

    email = EmailMessage(subject, messageHtml ,to=idcorreoJefatura)
    email.content_subtype='html'
    email.send()


def download_file(request, *args, **kwargs):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = kwargs['path']
    # Define the full file path
    filepath = BASE_DIR + '/documents/compromisos/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response

# def download_file(request,  **kwargs):
#     path = kwargs['path']
#     BASE_DIR = settings.BASE_DIR
#     file_path = os.path.join(BASE_DIR + '\documents\compromisos', path)
#     with open(file_path, 'rb') as fh:
#         response = HttpResponse(fh.read(), content_type="application/force-download")
#         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#         return response

