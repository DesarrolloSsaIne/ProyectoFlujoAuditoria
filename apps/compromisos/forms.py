from django import forms
from apps.compromisos.models import Ges_Compromisos
from apps.estado_compromiso.models import Glo_Estado_Compromiso
from apps.jefaturas.models import Ges_Jefatura
from apps.hallazgos.models import Ges_Hallazgo
from apps.registration.models import UsuariosExcepcion

from django.contrib.auth.models import User, Group
from django.db.models import Q

class DateInput(forms.DateInput):
    input_type = 'date'

class CompromisoAddForm(forms.ModelForm):


    class Meta:
        model = Ges_Compromisos

        fields = [
            'descripcion_compromiso',
            'medio_verificacion',
            'plazo_implementacion',
            'comentario_compromiso',





        ]


        widgets = {

            'descripcion_compromiso': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;', 'required':'required' }),
            'medio_verificacion': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;', 'required':'required' }),
            'plazo_implementacion': DateInput(attrs={'class': 'form-control', 'required':'required' }),
            'comentario_compromiso': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;'}),





        }

class CompromisoEditForm(forms.ModelForm):

    plazo_implementacion = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=('%Y-%m-%d',)
    )


    class Meta:
        model = Ges_Compromisos

        fields = [
            'descripcion_compromiso',
            'medio_verificacion',
            'plazo_implementacion',
            'comentario_compromiso',
            'comentario_auditor',

        ]


        widgets = {

            'descripcion_compromiso': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;', 'required':'required'}),
            'medio_verificacion': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;', 'required':'required'}),
            'comentario_compromiso': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;', 'required':'required'}),
            'comentario_auditor': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;'}),

        }

class CompromisoValidaFormAuditor(forms.ModelForm):

    plazo_implementacion = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=('%Y-%m-%d',)
    )


    class Meta:
        model = Ges_Compromisos

        fields = [
            'id',
            'descripcion_compromiso',
            'medio_verificacion',
            'plazo_implementacion',
            'comentario_compromiso',
            'comentario_auditor',

        ]


        widgets = {

            'descripcion_compromiso': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;' , 'readonly': 'readonly'}),
            'medio_verificacion': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;', 'readonly': 'readonly'}),
            'comentario_compromiso': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;', 'readonly': 'readonly'}),
            'comentario_auditor': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;'}),

        }


class CompromisoResponsableEditForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CompromisoResponsableEditForm, self).__init__(*args, **kwargs)

        #en_grupo=list(Group.objects.values_list('user', flat=True))
        cuentas_genericas=list(UsuariosExcepcion.objects.values_list('username', flat=True))
        cuentas_genericas_id = list(User.objects.values_list('id', flat=True).filter(username__in=cuentas_genericas))
        self.fields['responsable_hallazgo'].queryset = User.objects.all().exclude(Q(id__in=cuentas_genericas_id) | Q(first_name='geoportal')).order_by('username')

    class Meta:
        model = Ges_Compromisos

        fields = [

            'responsable_hallazgo',
            'cargo_responsable_id',

        ]


        widgets = {


            'responsable_hallazgo': forms.Select(attrs={'class': 'form-control', 'id': 'siteID'}),
            'cargo_responsable_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID2'}),




        }

class HallazgoAsignaEncargadoGestion(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(HallazgoAsignaEncargadoGestion, self).__init__(*args, **kwargs)

        #en_grupo=list(Group.objects.values_list('user', flat=True))
        cuentas_genericas=list(UsuariosExcepcion.objects.values_list('username', flat=True))
        cuentas_genericas_id = list(User.objects.values_list('id', flat=True).filter(username__in=cuentas_genericas))
        self.fields['enc_gestion_id'].queryset = User.objects.all().exclude(Q(id__in=cuentas_genericas_id) | Q(first_name='geoportal')).order_by('username')


    class Meta:
        model = Ges_Hallazgo

        fields = [

            'enc_gestion_id',


        ]

        widgets = {

            'enc_gestion_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID'}),

        }


class CompromisoEnviarRevisionForm(forms.ModelForm):

    class Meta:
        model = Ges_Compromisos

        fields = [

        ]

        widgets = {

        }


class CompromisoEditFormEstado(forms.ModelForm):
    class Meta:
        model = Ges_Compromisos
        fields = [

        ]
        widgets = {

        }