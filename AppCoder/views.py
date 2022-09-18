from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
# Create your views here.


def curso(request):

  materia = Curso(nombre = "Hacking", camada = 99999)

  materia.save()

  return HttpResponse(f"Estoy guardando el primer curso: {materia.nombre}")


def entregables(request):

  ente1 = Entregable(nombre = "Examen1", fechaEntrega = ("1967-10-23"))

  ente1.save()

  return HttpResponse(f"Mi nombre es {ente1.nombre} y entregue el dia {ente1.fechaEntrega}")

