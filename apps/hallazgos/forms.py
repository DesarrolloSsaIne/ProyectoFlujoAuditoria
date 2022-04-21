from django import forms
from apps.hallazgos.models import Ges_Hallazgo
from django.contrib.auth.models import User, Group
from django.db.models import Q
from apps.registration.models import UsuariosExcepcion
class DateInput(forms.DateInput):
    input_type = 'date'

class HallazgoAddForm(forms.ModelForm):
    TRUE_FALSE_CHOICES = (
        ('SI', 'SI'),
        ('No', 'No'),
    )

    TRUE_FALSE_CHOICES_NATURALEZA = (
        ('Gobierno Corporativo', 'Gobierno Corporativo'),
        ('Gestión de Riesgos', 'Gestión de Riesgos'),
        ('Control', 'Control'),
        ('No Aplica', 'No Aplica.'),

    )

    TRUE_FALSE_CHOICES_CRITICIDAD = (
        ('Alta', 'Criticidad Alta'),
        ('Media', 'Criticidad Media'),
        ('Baja', 'Criticidad Baja'),
    )

    sumario = forms.ChoiceField(choices=TRUE_FALSE_CHOICES,
                                widget=forms.Select(attrs={'class': 'form-control'}))

    naturaleza = forms.ChoiceField(choices=TRUE_FALSE_CHOICES_NATURALEZA,
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    opinion = forms.ChoiceField(choices=TRUE_FALSE_CHOICES_CRITICIDAD,
                                widget=forms.Select(attrs={'class': 'form-control'}))


    class Meta:
        model = Ges_Hallazgo

        fields = [
            'numero_hallazgo',
            'jefatura_id',
            'proceso',
            'naturaleza',
            'descripcion_hallazgo',
            'criterios',
            'causas',
            'efectos',
            'sumario',
            'recomendacion',
            'plazo',
            'opinion',
            'document',
            'cargo_responsable_id',


        ]


        widgets = {

            'numero_hallazgo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '5'}),
            'jefatura_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID'}),
            'proceso': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion_hallazgo': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;'}),
            'criterios': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;'}),
            'causas': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;'}),
            'efectos': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;'}),
            'recomendacion': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;'}),
            'plazo':  DateInput(attrs={'class': 'form-control'}),
            'cargo_responsable_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID2'}),



        }

class HallazgoUpdateForm(forms.ModelForm):
    TRUE_FALSE_CHOICES = (
        ('SI', 'SI'),
        ('No', 'No'),
    )

    TRUE_FALSE_CHOICES_NATURALEZA = (
        ('Gobierno Corporativo', 'Gobierno Corporativo'),
        ('Gestión de Riesgos', 'Gestión de Riesgos'),
        ('Control', 'Control'),
        ('No Aplica', 'No Aplica.'),

    )

    TRUE_FALSE_CHOICES_CRITICIDAD = (
        ('Alta', 'Criticidad Alta'),
        ('Media', 'Criticidad Media'),
        ('Baja', 'Criticidad Baja'),
    )

    sumario = forms.ChoiceField(choices=TRUE_FALSE_CHOICES,
                                       widget=forms.Select(attrs={'class': 'form-control'}))

    naturaleza = forms.ChoiceField(choices=TRUE_FALSE_CHOICES_NATURALEZA,
                                widget=forms.Select(attrs={'class': 'form-control'}))

    opinion = forms.ChoiceField(choices=TRUE_FALSE_CHOICES_CRITICIDAD,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    plazo = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=('%Y-%m-%d',)
    )


    class Meta:
        model = Ges_Hallazgo

        fields = [
            'numero_hallazgo',
            'jefatura_id',
            'proceso',
            'naturaleza',
            'descripcion_hallazgo',
            'criterios',
            'causas',
            'efectos',
            'sumario',
            'recomendacion',
            'plazo',
            'opinion',
            'document',
            'cargo_responsable_id',



        ]



        widgets = {

            'numero_hallazgo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '5','id': 'txt_numero'}),
            'jefatura_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID'}),
            'proceso': forms.TextInput(attrs={'class': 'form-control', 'id': 'txt_proceso'}),
            'descripcion_hallazgo': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_descripcion'}),
            'criterios': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_criterios'}),
            'causas': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_causas'}),
            'efectos': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_efectos'}),
            'recomendacion': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_recomendacion'}),
            'cargo_responsable_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID2'}),



        }


class HallazgoDetalleDirectorForm(forms.ModelForm):
    TRUE_FALSE_CHOICES = (
        ('SI', 'SI'),
        ('No', 'No'),
    )

    TRUE_FALSE_CHOICES_NATURALEZA = (
        ('Gobierno Corporativo', 'Gobierno Corporativo'),
        ('Gestión de Riesgos', 'Gestión de Riesgos'),
        ('Control', 'Control'),
        ('No Aplica', 'No Aplica.'),

    )

    TRUE_FALSE_CHOICES_CRITICIDAD = (
        ('Alta', 'Criticidad Alta'),
        ('Media', 'Criticidad Media'),
        ('Baja', 'Criticidad Baja'),
    )

    sumario = forms.ChoiceField(choices=TRUE_FALSE_CHOICES,
                                       widget=forms.Select(attrs={'class': 'form-control', 'disabled':'true'}))

    naturaleza = forms.ChoiceField(choices=TRUE_FALSE_CHOICES_NATURALEZA,
                                widget=forms.Select(attrs={'class': 'form-control', 'disabled':'true'}))

    opinion = forms.ChoiceField(choices=TRUE_FALSE_CHOICES_CRITICIDAD,
                                widget=forms.Select(attrs={'class': 'form-control', 'disabled':'true'}))
    plazo = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=('%Y-%m-%d',)
    )



    class Meta:
        model = Ges_Hallazgo

        fields = [
            'numero_hallazgo',
            'jefatura_id',
            'proceso',
            'naturaleza',
            'descripcion_hallazgo',
            'criterios',
            'causas',
            'efectos',
            'sumario',
            'recomendacion',
            'plazo',
            'opinion',
            'document',
            'cargo_responsable_id',



        ]



        widgets = {

            'numero_hallazgo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '5','id': 'txt_numero', 'disabled':'true'}),
            'jefatura_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID', 'disabled':'true'}),
            'proceso': forms.TextInput(attrs={'class': 'form-control', 'id': 'txt_proceso', 'disabled':'true'}),
            'descripcion_hallazgo': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_descripcion', 'disabled':'true'}),
            'criterios': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_criterios', 'disabled':'true'}),
            'causas': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_causas', 'disabled':'true'}),
            'efectos': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_efectos', 'disabled':'true'}),
            'recomendacion': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_recomendacion', 'disabled':'true'}),
            'cargo_responsable_id': forms.Select(attrs={'class': 'form-control', 'id': 'siteID2', 'disabled':'true'}),


        }


class HallazgoDetalleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
       super(HallazgoDetalleForm, self).__init__(*args, **kwargs)
       self.fields['jefatura_id'].widget.attrs['readonly'] = True
       self.fields['naturaleza'].widget.attrs['readonly'] = True
       self.fields['opinion'].widget.attrs['readonly'] = True
       self.fields['plazo'].widget.attrs['readonly'] = True
       self.fields['sumario'].widget.attrs['readonly'] = True


    TRUE_FALSE_CHOICES = (
        ('SI', 'SI'),
        ('No', 'No'),
    )

    TRUE_FALSE_CHOICES_NATURALEZA = (
        ('SI', 'Gobierno Corporativo'),
        ('No', 'Gestión de Riesgos'),
        ('SI', 'Control'),
        ('No', 'No Aplica.'),

    )

    TRUE_FALSE_CHOICES_CRITICIDAD = (
        ('Alta', 'Criticidad Alta'),
        ('Media', 'Criticidad Media'),
        ('Baja', 'Criticidad Baja'),
    )

    sumario = forms.ChoiceField(choices=TRUE_FALSE_CHOICES,
                                       widget=forms.Select(attrs={'class': 'form-control'}))

    naturaleza = forms.ChoiceField(choices=TRUE_FALSE_CHOICES_NATURALEZA,
                                widget=forms.Select(attrs={'class': 'form-control'}))

    opinion = forms.ChoiceField(choices=TRUE_FALSE_CHOICES_CRITICIDAD,
                                widget=forms.Select(attrs={'class': 'form-control'}))
    plazo = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=('%Y-%m-%d',)
    )

    class Meta:
        model = Ges_Hallazgo

        fields = [
            'numero_hallazgo',
            'jefatura_id',
            'proceso',
            'naturaleza',
            'descripcion_hallazgo',
            'criterios',
            'causas',
            'efectos',
            'sumario',
            'recomendacion',
            'plazo',
            'opinion',


        ]



        widgets = {

            'numero_hallazgo': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '2','id': 'txt_numero',  'readonly': 'readonly'}),
            'jefatura_id': forms.Select(attrs={'class': 'form-control'}),
            'proceso': forms.TextInput(attrs={'class': 'form-control', 'id': 'txt_proceso',  'readonly': 'readonly'}),
            'descripcion_hallazgo': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_descripcion',  'readonly': 'readonly'}),
            'criterios': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_criterios',  'readonly': 'readonly'}),
            'causas': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_causas',  'readonly': 'readonly'}),
            'efectos': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_efectos',  'readonly': 'readonly'}),
            'recomendacion': forms.Textarea(attrs={'class': 'form-control' , 'style': 'height:60px;', 'id': 'txt_recomendacion',  'readonly': 'readonly'}),



        }



