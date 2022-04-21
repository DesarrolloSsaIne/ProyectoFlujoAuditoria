from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from apps.auditoria.models import Ges_auditoria
from django.db.models import Count
from django.db.models import Q
# Create your views here.


class InicioDashboard(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(InicioDashboard, self).get_context_data(**kwargs)
        id_usuario_actual = self.request.user.id  # obtiene id usuario actual
        Grupo = Group.objects.get(user=self.request.user)

        self.request.session['grupo'] = str(Grupo)

        if Grupo.id==5:
            total_auditorias_abiertas = list(
                Ges_auditoria.objects.filter(estado_auditoria_id=1).aggregate(
                    Count('id')).values())[0]

            total_auditorias_cerradas= list(
                Ges_auditoria.objects.filter(estado_auditoria_id=2).aggregate(
                    Count('id')).values())[0]




            context['total_auditorias'] = {'abiertas': total_auditorias_abiertas,
                                           'cerradas': total_auditorias_cerradas}




            total_auditorias = list(Ges_auditoria.objects.filter().aggregate(Count('id')).values())[0]

            if total_auditorias ==0: #Para que no divida por 0 en el caso que no existan auditorias ingresadas.
                context['total_auditorias'] = {'total': 0}
                total_auditorias=1

            else:
                context['total_auditorias_suma'] = {'total': total_auditorias}

            total_auditorias_institucional = list(Ges_auditoria.objects.filter(
                Q(tipo_auditoria=1)).aggregate(Count('id')).values())[0]
            total_auditorias_ministerial = list(Ges_auditoria.objects.filter(
                Q(tipo_auditoria=2)).aggregate(Count('id')).values())[0]
            total_auditorias_gubernamental = list(Ges_auditoria.objects.filter(
                Q(tipo_auditoria=3)).aggregate(Count('id')).values())[0]
            total_auditorias_extraordinaria = list(Ges_auditoria.objects.filter(
                Q(tipo_auditoria=4)).aggregate(Count('id')).values())[0]
            total_auditorias_otra = list(Ges_auditoria.objects.filter(
                Q(tipo_auditoria=5)).aggregate(Count('id')).values())[0]


            context['auditorias'] = {'total_institucional': total_auditorias_institucional,
                                      'total_institucional_per': "{0:.2f}".format(((total_auditorias_institucional*100)/total_auditorias)),

                                      'total_ministerial': total_auditorias_ministerial,
                                      'total_ministerial_per': "{0:.2f}".format(
                                          ((total_auditorias_ministerial * 100) / total_auditorias)),

                                      'total_gubernamental': total_auditorias_gubernamental,
                                      'total_gubernamental_per': "{0:.2f}".format(
                                          ((total_auditorias_gubernamental * 100) / total_auditorias)),

                                      'total_extraordinaria': total_auditorias_extraordinaria,
                                      'total_extraordinaria_per': "{0:.2f}".format(
                                          ((total_auditorias_extraordinaria * 100) / total_auditorias)),

                                      'total_otra': total_auditorias_otra,
                                      'total_otra_per': "{0:.2f}".format(
                                          ((total_auditorias_otra * 100) / total_auditorias)),


                                      }




            context["GrupoDashboard"] = 'GrupoDirector'



            UnidadesAsociadas = Ges_auditoria.objects.filter().values(
                    'jefatura_id__id_nivel__descripcion_nivel').annotate(
                    CantidadPlan=Count('id')).order_by(
                    'jefatura_id')

            auditorias = list(Ges_auditoria.objects.filter( ).values_list(
                    'jefatura_id', flat=True).distinct().order_by(
                    'jefatura_id')) #trae todas las jefaturas diferentes

            ValAbiertas = []
            ValCerradas = []

            for i in auditorias:
                val = Ges_auditoria.objects.filter(
                        Q(jefatura_id=i)  & Q(estado_auditoria_id=1)).count()
                ValAbiertas.append(val)

                val = Ges_auditoria.objects.filter(
                        Q(jefatura_id=i)  & Q(estado_auditoria_id=2)).count()
                ValCerradas.append(val)

            context["valores"] = {"ValAbiertas": ValAbiertas,
                                      "ValCerradas": ValCerradas,
                                      }

            context["UnidadesAsociadas"] = UnidadesAsociadas

            return context


    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        template_name = self.template_name

        Grupo = Group.objects.get(user=self.request.user)

        if Grupo.id==1:  # Si pertenece a un usuario admin, plani y super
            template_name = 'dashboard/dashboard_admin.html'

        if Grupo.id==2:  # Si pertenece a un usuario admin, plani y super
            template_name = 'dashboard/dashboard_admin.html'

        if Grupo.id==3:  # Si pertenece a un usuario admin, plani y super
            template_name = 'dashboard/dashboard_admin.html'

        if Grupo.id==4:  # Si pertenece a un usuario admin, plani y super
            template_name = 'dashboard/dashboard_admin.html'

        if Grupo.id==5:  # Si pertenece a un usuario admin, plani y super
            template_name = 'dashboard/dashboard_director.html'


        # if Grupo.id == 1:  # Si pertenece a un usuario que formula
        #     template_name = 'dashboard/dashboard_formulador.html'
        #
        # if Grupo.id == 3:  # Si pertenece a jefatura primer nivel
        #     template_name = 'dashboard/dashboard_jefeprimer.html'
        #
        # if Grupo.id == 4:  # Si pertenece a jefatura segundo nivel
        #     template_name = 'dashboard/dashboard_jefesegundo.html'


        return render(request, template_name, context)