from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
# each function of this file is a view

def saludo(request):
    return HttpResponse("<hmtl><body><h1>Purueba de Luis Nyanniel Moreno UwUmaría!</hmtl></body></h1>")

def despedida(resquest):
    return HttpResponse("sayonara UwU")

def authPage(request):
    doc_externo=open('/home/luisdogo/Desktop/schoom_root/schoom/authPage/test.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    ctx=Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)