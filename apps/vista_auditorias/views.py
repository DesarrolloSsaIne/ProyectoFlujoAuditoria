from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from apps.auditoria.models import Ges_auditoria
from apps.compromisos.models import Ges_Compromisos
from apps.estructura_jerarquica.models import Ges_Niveles, Ges_CuartoNivel, Ges_TercerNivel, Ges_SegundoNivel, Ges_PrimerNivel
from apps.hallazgos.models import Ges_Hallazgo
from apps.jefaturas.models import Ges_Jefatura
from django.db.models import Case, CharField, Value, When, OuterRef, Count, Subquery
from django.template import loader
from django.http import HttpResponse


def listarNivelUsuario(request):

    id_usuario_actual= request.user.id #obtiene id usuario actual

    nivel_usuario= Ges_Jefatura.objects.get(id_user=id_usuario_actual)
    orden_nivel =nivel_usuario.id_nivel.orden_nivel
    id_nivel = nivel_usuario.id_nivel.id

    Nivelist = Ges_Niveles.objects.filter(id=id_nivel).annotate(
        nivel_order=Case(
            When(orden_nivel=1, then='id_primer_nivel'),
            When(orden_nivel=2, then='id_segundo_nivel'),
            When(orden_nivel=3, then='id_tercer_nivel'),
            When(orden_nivel=4, then='id_cuarto_nivel'),
            output_field=CharField(),
        )
    )
    for nivel in Nivelist:
        id_estructura_final = nivel.nivel_order

    if  orden_nivel == 1:
        count_auditorias = Ges_auditoria.objects.values('jefatura_id').filter(
            jefatura_id=nivel_usuario.id).annotate(
            count_id_auditoria=Count('id'))

        Ges_Nivel_detail = Ges_PrimerNivel.objects.filter(id=id_estructura_final).annotate(
        count_auditorias=Subquery(count_auditorias.values('count_id_auditoria')))
        template = 'vista_auditorias/vista_primer_nivel.html'

    if orden_nivel == 2:
        count_auditorias = Ges_auditoria.objects.values('jefatura_id').filter(
            jefatura_id=nivel_usuario.id).annotate(
            count_id_auditoria=Count('id'))

        Ges_Nivel_detail = Ges_SegundoNivel.objects.filter(id=id_estructura_final).annotate(
        count_auditorias=Subquery(count_auditorias.values('count_id_auditoria')))
        template = 'vista_auditorias/vista_segundo_nivel.html'
    if  orden_nivel ==3:
        count_auditorias = Ges_auditoria.objects.values('jefatura_id').filter(
            jefatura_id=nivel_usuario.id).annotate(
            count_id_auditoria=Count('id'))

        Ges_Nivel_detail = Ges_TercerNivel.objects.filter(id=id_estructura_final).annotate(
        count_auditorias=Subquery(count_auditorias.values('count_id_auditoria')))
        template = 'vista_auditorias/vista_tercer_nivel.html'
    if  orden_nivel == 4:
        count_auditorias = Ges_auditoria.objects.values('jefatura_id').filter(
            jefatura_id=nivel_usuario.id).annotate(
            count_id_auditoria=Count('id'))

        Ges_Nivel_detail = Ges_CuartoNivel.objects.filter(id=id_estructura_final).annotate(
        count_auditorias=Subquery(count_auditorias.values('count_id_auditoria')))
        template = 'vista_auditorias/vista_cuarto_nivel.html'

    return render(
        request,
        template,
        context={'ObjectList': Ges_Nivel_detail}
    )

def listarPrimerNivel(request):



        Ges_PrimerNivel_detail = Ges_PrimerNivel.objects.all()
        t = loader.get_template('vista_auditorias/vista_primer_nivel.html')
        c = {'ObjectList': Ges_PrimerNivel_detail}

        return HttpResponse(t.render(c, request), content_type='text/html; charset=utf-8')

def listarSegundoNivel(request, pk):


        Ges_SegundoNivel_detail = Ges_SegundoNivel.objects.raw('SELECT pn.id, pn.descripcion_nivel,' +
                                                                '(SELECT COUNT(id) FROM auditoria_ges_auditoria  au WHERE au.jefatura_id_id = j.id ) ' +
                                                                'as count ' +
                                                                'FROM  estructura_jerarquica_ges_segundonivel pn INNER JOIN ' +
                                                                'estructura_jerarquica_ges_niveles gn ON pn.id = gn.id_segundo_nivel_id ' +
                                                                'LEFT outer JOIN jefaturas_ges_jefatura j ON j.id_nivel_id = gn.id ' +
                                                                'LEFT OUTER JOIN auditoria_ges_auditoria a ON a.jefatura_id_id = j.id ' +
                                                                'WHERE pn.primer_nivel_id ='+ str(pk))

        t = loader.get_template('vista_auditorias/vista_segundo_nivel.html')
        c = {'ObjectList': Ges_SegundoNivel_detail}
        return HttpResponse(t.render(c, request), content_type='text/html; charset=utf-8')

def listarTercerNivel(request, pk):

        Ges_SegundoNivel_detail = Ges_TercerNivel.objects.raw('SELECT pn.id, pn.descripcion_nivel, '+
                                                              '(SELECT COUNT(id) FROM auditoria_ges_auditoria  au WHERE au.jefatura_id_id = j.id ) '+
                                                                'as count ' +
                                                                'FROM  estructura_jerarquica_ges_tercernivel pn  INNER JOIN '+
                                                                'estructura_jerarquica_ges_niveles gn ON pn.id = gn.id_tercer_nivel_id '+
                                                                'LEFT outer JOIN jefaturas_ges_jefatura j ON j.id_nivel_id = gn.id '+
                                                                'LEFT OUTER JOIN auditoria_ges_auditoria a ON a.jefatura_id_id = j.id '+
                                                                'WHERE pn.segundo_nivel_id ='+  str(pk))
        t = loader.get_template('vista_auditorias/vista_tercer_nivel.html')
        c = {'ObjectList': Ges_SegundoNivel_detail, }
        request.session['idTercerNivel'] = pk

        return HttpResponse(t.render(c, request), content_type='text/html; charset=utf-8')

def listarCuartoNivel(request, pk):

        Ges_CuartoNivel_detail = Ges_CuartoNivel.objects.raw('SELECT pn.id, pn.descripcion_nivel, '+
                                                            '(SELECT COUNT(id) FROM auditoria_ges_auditoria  au WHERE au.jefatura_id_id = j.id ) '+
                                                            'as count '+
                                                            'FROM  estructura_jerarquica_ges_cuartonivel pn  INNER JOIN '+
                                                            'estructura_jerarquica_ges_niveles gn ON pn.id = gn.id_cuarto_nivel_id '+
                                                            'LEFT outer JOIN jefaturas_ges_jefatura j ON j.id_nivel_id = gn.id '+
                                                            'LEFT OUTER JOIN auditoria_ges_auditoria a ON a.jefatura_id_id = j.id ' +
                                                            'WHERE pn.tercer_nivel_id ='+ str(pk))
        return render(
            request,
            'vista_auditorias/vista_cuarto_nivel.html',
            context={'ObjectList': Ges_CuartoNivel_detail}
        )

class AuditoriaListVista(ListView):
    model = Ges_auditoria
    template_name = 'vista_auditorias/auditoria_list_vista.html'




    def get_context_data(self, **kwargs):
        context = super(AuditoriaListVista, self).get_context_data(**kwargs)
        id_nivel = self.kwargs['pk']
        orden_nivel = int(self.kwargs['orden'])

        if orden_nivel == 1:
           nivel_jefatura = Ges_Niveles.objects.get(id_primer_nivel_id = id_nivel)
        if orden_nivel == 2:
            nivel_jefatura = Ges_Niveles.objects.get(id_segundo_nivel_id=id_nivel)
        if orden_nivel == 3:
            nivel_jefatura = Ges_Niveles.objects.get(id_tercer_nivel_id=id_nivel)
        if orden_nivel == 4:
            nivel_jefatura = Ges_Niveles.objects.get(id_cuarto_nivel_id=id_nivel)


        jefatura_id = Ges_Jefatura.objects.get(id_nivel_id=nivel_jefatura.id)



        count_hallazgos = Ges_Hallazgo.objects.values('id_auditoria').filter(
            id_auditoria=OuterRef('pk')).annotate(
            count_id_auditoria=Count('id_auditoria'))

        lista_auditorias = Ges_auditoria.objects.filter(jefatura_id = jefatura_id).annotate(
        count_hallazgos=Subquery(count_hallazgos.values('count_id_auditoria')))

        context['object_list'] = lista_auditorias
        self.request.session['id_jef'] = id_nivel
        self.request.session['nivel'] = orden_nivel



        return context

class HallazgosList(ListView):
    model = Ges_Hallazgo
    template_name = 'vista_auditorias/hallazgos_list_vista.html'

    def get_context_data(self, **kwargs):
        context = super(HallazgosList, self).get_context_data(**kwargs)

        lista_hallazgos = Ges_Hallazgo.objects.filter(id_auditoria_id=self.kwargs['pk'])
        auditoria = Ges_auditoria.objects.get(id=self.kwargs['pk'])
        context['object_list'] = lista_hallazgos

        id_nivel=self.request.session['id_jef']
        orden_nivel=self.request.session['nivel']
        context['nom_auditoria'] = {'nombre': str(auditoria.descripcion_auditoria), 'id_nivel':id_nivel,'orden_nivel':orden_nivel}

        self.request.session['pk_auditoria'] = self.kwargs['pk']
        return context

class ComprimisoList(ListView):
    model = Ges_Compromisos
    template_name = 'vista_auditorias/compromisos_list_vista.html'

    def get_context_data(self,  **kwargs):
        context = super(ComprimisoList, self).get_context_data(**kwargs)

        lista_compromisos = Ges_Compromisos.objects.filter(hallazgo_id=self.kwargs['pk'])
        #auditoria = Ges_auditoria.objects.get(id=self.kwargs['pk'])
        hallazgo =  Ges_Hallazgo.objects.get(id=self.kwargs['pk'])
        context['object_list'] = lista_compromisos
        context['auditoria'] ={ 'id_hallazgo':hallazgo.id_auditoria_id, 'nombre' : str(hallazgo.id_auditoria.descripcion_auditoria), 'numero' : str(hallazgo.id_auditoria.cod_auditoria) }

        self.request.session['pk_hallazgo'] = self.kwargs['pk']
        return context