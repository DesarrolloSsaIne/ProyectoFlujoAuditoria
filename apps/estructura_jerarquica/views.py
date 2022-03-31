from django.template import loader
from django.http import HttpResponse
from apps.estructura_jerarquica.models import  Ges_SegundoNivel,Ges_PrimerNivel, Ges_TercerNivel, Ges_CuartoNivel
from django.shortcuts import render

def listarPrimerNivel(request):

    Ges_PrimerNivel_detail = Ges_PrimerNivel.objects.all()
    t = loader.get_template('estructura/listar_primer_nivel.html')
    c = {'ObjectList': Ges_PrimerNivel_detail}

    return HttpResponse(t.render(c, request), content_type='text/html; charset=utf-8')

def listarSegundoNivel(request, pk):

    Ges_SegundoNivel_detail = Ges_SegundoNivel.objects.filter(primer_nivel_id=pk)
    t = loader.get_template('estructura/listar_segundo_nivel.html')
    c = {'ObjectList': Ges_SegundoNivel_detail}
    return HttpResponse(t.render(c, request), content_type='text/html; charset=utf-8')

def listarTercerNivel(request, pk):

    Ges_SegundoNivel_detail = Ges_TercerNivel.objects.filter(segundo_nivel_id=pk)
    t = loader.get_template('estructura/listar_tercer_nivel.html')
    c = {'ObjectList': Ges_SegundoNivel_detail, }
    request.session['idTercerNivel']=pk

    return HttpResponse(t.render(c, request), content_type='text/html; charset=utf-8')

def listarCuartoNivel(request,pk):

     Ges_CuartoNivel_detail = Ges_CuartoNivel.objects.filter(tercer_nivel_id=pk)




     return render(
        request,
        'estructura/listar_cuarto_nivel.html',
        context={'ObjectList':Ges_CuartoNivel_detail,
         'idTercerNivel':request.session['idTercerNivel'] }
        )

