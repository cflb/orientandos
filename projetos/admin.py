from django.contrib import admin
from .models import Aluno, Projeto

# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'turma', 'ano', 'projeto')
    list_filter = ('turma', 'ano')
    

class ProjetoAdmin(admin.ModelAdmin):
    fields = ['titulo', 'resumo', 'documento', ('data_inicio','data_fim'), 'status']
    list_filter = ('data_inicio','data_fim')

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Projeto, ProjetoAdmin)