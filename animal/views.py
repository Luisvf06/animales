from django.shortcuts import render
from .models import Animal
from .models import Colaborador
from .models import Protectora
# Create your views here.
def animal_list(request):
    animales = Animal.objects.all()
    return render(request,'animal/animal.html',{'animal_mostrar':animales})

def colaborador_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request,'animal/colaborador.html',{'colaborador_mostrar':colaboradores})

def protectora_list(request):
    protectoras = Protectora.objects.all()
    return render(request,'<animal/protectora.html',{'protectora_mostrar':protectoras})