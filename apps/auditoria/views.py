from django.shortcuts import render
from apps.auditoria.models import Ges_auditoria, Glo_autoria_auditor
from apps.hallazgos.models import Ges_Hallazgo
from apps.auditoria.forms import AuditoriaAddForm, AuditoriaUpdForm, AuditoriaAuditorAddForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models.deletion import ProtectedError
from django.db.models import Subquery, OuterRef, Count,F #import agregado por JR- sprint 8 - Ok
from django.db.models.functions import Concat
from apps.periodos.models import Glo_Periodos
from django.contrib.auth.models import User, Group
# Create your views here.


class AuditoriaList(ListView):
    model = Ges_auditoria
    template_name = 'auditoria/auditoria_list.html'

    def get_context_data(self, **kwargs):
        context = super(AuditoriaList, self).get_context_data(**kwargs)

        # lista_auditorias = Ges_auditoria.objects.all()
        id_usuario = self.request.user.id
        auditarias_usuario = Glo_autoria_auditor.objects.filter(id_auditor_id = id_usuario)
        a_list = []
        for auditarias in auditarias_usuario:
            a_list.append(auditarias.id_auditoria_id)


        count_auditores = Glo_autoria_auditor.objects.values('id_auditoria').filter(
            id_auditoria=OuterRef('pk')).annotate(
            count_id_auditoria=Count('id_auditoria'))

        count_hallazgos = Ges_Hallazgo.objects.values('id_auditoria').filter(
            id_auditoria=OuterRef('pk')).annotate(
            count_id_auditoria=Count('id_auditoria'))

        lista_auditorias = Ges_auditoria.objects.filter(id__in = a_list).annotate(
            count_auditores=Subquery(count_auditores.values('count_id_auditoria')),
        count_hallazgos=Subquery(count_hallazgos.values('count_id_auditoria')))

        context['object_list'] = lista_auditorias

        return context


class AuditoriaDelete(SuccessMessageMixin, DeleteView ):
    model = Ges_auditoria
    template_name = 'auditoria/auditoria_delete.html'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            obj.delete()


            request.session['message_class'] = "alert alert-success"
            messages.success(self.request, "El registro fue eliminado correctamente!")
            return HttpResponseRedirect('/auditorias/listar/')

        except ProtectedError as e:
            request.session['message_class'] = "alert alert-danger"
            messages.error(request, "Error de integridad: No se puede eliminar esta auditoría porque tiene registros asociados.")
            return HttpResponseRedirect('/auditorias/listar/')

        except Exception  as e:
            request.session['message_class'] = "alert alert-danger"
            messages.error(request, "Error interno: No se ha eliminado el registro. Comuníquese con el administrador.")
            return HttpResponseRedirect('/auditorias/listar/')



class AuditoriaCreate(SuccessMessageMixin, CreateView):
    model = Ges_auditoria
    form_class = AuditoriaAddForm
    template_name = 'auditoria/auditoria_form.html'
   # success_url = reverse_lazy('feriados_list')


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():
            form.instance.estado_auditoria_id = '1'
            task = form.save()
            pk = task.id
            agregarReposanble(self.request.user.id,pk )
            request.session['message_class'] = "alert alert-success"
            messages.success(self.request, "Los datos fueron creados correctamente!")
            return HttpResponseRedirect('/auditorias/listar/')
        else:
            request.session['message_class'] = "alert alert-danger"
            messages.error(self.request, "Error interno: No se ha creado el registro. Comuníquese con el administrador.")
            return HttpResponseRedirect('/auditorias/listar/')

def agregarReposanble(id_usuario , id_auditoria):

    Glo_autoria_auditor.objects.create(

        id_auditor_id=id_usuario,
        id_auditoria_id =id_auditoria,
    )
    return None

class AuditoriaUpdate(SuccessMessageMixin, UpdateView ):
    model = Ges_auditoria
    form_class = AuditoriaUpdForm
    template_name = 'auditoria/auditoria_form_update.html'

    def post(self, request, *args, **kwargs):

        self.object = self.get_object
        id = kwargs['pk']
        id_auditoria = self.model.objects.get(id=id)
        form = self.form_class(request.POST, instance=id_auditoria)

        if form.is_valid():
            form.save()
            request.session['message_class'] = "alert alert-success"
            messages.success(self.request, "Los datos fueron actualizados correctamente!" )
            return HttpResponseRedirect('/auditorias/listar/')
        else:
            request.session['message_class'] = "alert alert-danger"
            messages.error(self.request, "Error interno: No se ha actualizado el registro. Comuníquese con el administrador.")
            return HttpResponseRedirect('/auditorias/listar/')


class AuditoriaAuditoresList(ListView):
    model = Ges_auditoria
    template_name = 'auditoria/auditoria_auditores_list.html'

    def get_context_data(self,  **kwargs):
        context = super(AuditoriaAuditoresList, self).get_context_data(**kwargs)

        lista_auditorias = Glo_autoria_auditor.objects.filter(id_auditoria_id=self.kwargs['pk'])

        context['object_list'] = lista_auditorias

        self.request.session['pk_auditoria'] = self.kwargs['pk']


        return context




class AuditoriaAuditorCreate(SuccessMessageMixin, CreateView):
    model = Glo_autoria_auditor
    form_class = AuditoriaAuditorAddForm
    template_name = 'auditoria/auditoria_auditor_form.html'
   # success_url = reverse_lazy('feriados_list')


    def get_form_kwargs(self, **kwargs):
        kwargs = super(AuditoriaAuditorCreate, self).get_form_kwargs()
        kwargs['id_auditoria'] = self.request.session['pk_auditoria']
        return kwargs


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        if form.is_valid():

            form.instance.id_auditoria_id = self.request.session['pk_auditoria']

            form.save()
            request.session['message_class'] = "alert alert-success"
            messages.success(self.request, "Los datos fueron creados correctamente!")
            return HttpResponseRedirect('/auditorias/listaAuditores/' + self.request.session['pk_auditoria'])
        else:
            request.session['message_class'] = "alert alert-danger"
            messages.error(self.request, "Error interno: No se ha creado el registro. Comuníquese con el administrador.")
            return HttpResponseRedirect('/auditorias/listaAuditores/' +self.request.session['pk_auditoria'])



class AuditoriaAuditorDelete(SuccessMessageMixin, DeleteView ):
    model = Glo_autoria_auditor
    template_name = 'auditoria/auditoria_auditor_delete.html'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            obj.delete()


            request.session['message_class'] = "alert alert-success"
            messages.success(self.request, "El registro fue eliminado correctamente!")
            return HttpResponseRedirect('/auditorias/listaAuditores/' + self.request.session['pk_auditoria'])

        except ProtectedError as e:
            request.session['message_class'] = "alert alert-danger"
            messages.error(request, "Error de integridad: No se puede eliminar esta auditoría porque tiene registros asociados.")
            return HttpResponseRedirect('/auditorias/listaAuditores/' + self.request.session['pk_auditoria'])

        except Exception  as e:
            request.session['message_class'] = "alert alert-danger"
            messages.error(request, "Error interno: No se ha eliminado el registro. Comuníquese con el administrador.")
            return HttpResponseRedirect('/auditorias/listaAuditores/' + self.request.session['pk_auditoria'])