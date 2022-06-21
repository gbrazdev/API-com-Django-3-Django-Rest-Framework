from django.contrib import admin
from escola.models import Aluno, Curso


class Alunos(admin.ModelAdmin) :
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    lister_per_page = 20


admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin) :
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel',)
    list_display_links = ('id', 'descricao')
    search_fields = ('codigo_curso',)
    lister_per_page = 20


admin.site.register(Curso, Cursos)


