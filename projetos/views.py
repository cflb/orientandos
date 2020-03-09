from django.shortcuts import render
from .models import Projeto

# Create your views here.
def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos.html', {'projetos': projetos})

def lista_alunos(request):
    pass