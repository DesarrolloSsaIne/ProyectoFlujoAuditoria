from django import forms
from apps.auditoria.models import Ges_auditoria, Glo_autoria_auditor
from django.contrib.auth.models import User, Group
from django.db.models import Q

class DateInput(forms.DateInput):
    input_type = 'date'

class AuditoriaAddForm(forms.ModelForm):

    TRUE_FALSE_CHOICES = (
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026'),
        (2027, '2027'),
        (2028, '2028'),
        (2029, '2029'),
        (2030, '2030'),
        (2031, '2031'),
        (2032, '2032'),
        (2033, '2033'),
        (2034, '2034'),
        (2035, '2035'),
        (2036, '2036'),
        (2037, '2037'),
        (2038, '2038'),
        (2039, '2039'),
        (2040, '2040'),
    )
    anio_auditoria = forms.ChoiceField(choices=TRUE_FALSE_CHOICES,
                                   widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = Ges_auditoria

        fields = [
            'cod_auditoria',
            'jefatura_id',
            'anio_auditoria',
            'descripcion_auditoria',
            'alcance_auditoria',
            'tipo_auditoria',
            'fecha_inicio_auditoria',



        ]


        widgets = {

            'cod_auditoria': forms.TextInput(attrs={'class': 'form-control'}),
            'jefatura_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID'}),
            'descripcion_auditoria': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;'}),
            'alcance_auditoria': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;'}),
            'tipo_auditoria': forms.Select(attrs={'class': 'form-control'}),
            'fecha_inicio_auditoria': DateInput(attrs={'class': 'form-control'}),


        }



class AuditoriaUpdForm(forms.ModelForm):

    TRUE_FALSE_CHOICES = (
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026'),
        (2027, '2027'),
        (2028, '2028'),
        (2029, '2029'),
        (2030, '2030'),
        (2031, '2031'),
        (2032, '2032'),
        (2033, '2033'),
        (2034, '2034'),
        (2035, '2035'),
        (2036, '2036'),
        (2037, '2037'),
        (2038, '2038'),
        (2039, '2039'),
        (2040, '2040'),
    )
    anio_auditoria = forms.ChoiceField(choices=TRUE_FALSE_CHOICES,
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    fecha_inicio_auditoria = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=('%Y-%m-%d',)
    )



    class Meta:
        model = Ges_auditoria

        fields = [
            'cod_auditoria',
            'jefatura_id',
            'anio_auditoria',
            'descripcion_auditoria',
            'alcance_auditoria',
            'tipo_auditoria',
            'fecha_inicio_auditoria',



        ]

        widgets = {

            'cod_auditoria': forms.TextInput(attrs={'class': 'form-control'}),
            'jefatura_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID'}),
            'descripcion_auditoria': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;'}),
            'alcance_auditoria': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;'}),
            'tipo_auditoria': forms.Select(attrs={'class': 'form-control'}),


        }


class AuditoriaAuditorAddForm(forms.ModelForm):


    def __init__(self, id_auditoria,*args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(AuditoriaAuditorAddForm, self).__init__(*args, **kwargs)

        seleccionados= list(Glo_autoria_auditor.objects.values_list('id_auditor', flat=True).filter(id_auditoria=id_auditoria))

        auditores=list(User.objects.values_list('id', flat=True).filter(groups__in=Group.objects.filter(id='2')).exclude(id__in=seleccionados))

        self.fields['id_auditor'].queryset = User.objects.filter(id__in=auditores).order_by('username')





    class Meta:
        model = Glo_autoria_auditor

        fields = [
            'id_auditor',



        ]

        widgets = {


            'id_auditor': forms.Select(attrs={'class': 'form-control', 'id': 'siteID'}),


        }


class AuditoriaDetalleDirectorForm(forms.ModelForm):

    TRUE_FALSE_CHOICES = (
        (2021, '2021'),
        (2022, '2022'),
        (2023, '2023'),
        (2024, '2024'),
        (2025, '2025'),
        (2026, '2026'),
        (2027, '2027'),
        (2028, '2028'),
        (2029, '2029'),
        (2030, '2030'),
        (2031, '2031'),
        (2032, '2032'),
        (2033, '2033'),
        (2034, '2034'),
        (2035, '2035'),
        (2036, '2036'),
        (2037, '2037'),
        (2038, '2038'),
        (2039, '2039'),
        (2040, '2040'),
    )
    anio_auditoria = forms.ChoiceField(choices=TRUE_FALSE_CHOICES,
                                   widget=forms.Select(attrs={'class': 'form-control', 'disabled':'true'}))

    fecha_inicio_auditoria = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=('%Y-%m-%d',)
    )



    class Meta:
        model = Ges_auditoria

        fields = [
            'cod_auditoria',
            'jefatura_id',
            'anio_auditoria',
            'descripcion_auditoria',
            'alcance_auditoria',
            'tipo_auditoria',
            'fecha_inicio_auditoria',



        ]

        widgets = {

            'cod_auditoria': forms.TextInput(attrs={'class': 'form-control', 'readonly':'readonly'}),
            'jefatura_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID', 'disabled':'true'}),
            'descripcion_auditoria': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;', 'readonly':'readonly'}),
            'alcance_auditoria': forms.Textarea(attrs={'class': 'form-control', 'style': 'height:60px;', 'readonly':'readonly'}),
            'tipo_auditoria': forms.Select(attrs={'class': 'form-control', 'disabled':'true'}),


        }
