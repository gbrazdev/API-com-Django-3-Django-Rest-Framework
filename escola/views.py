from rest_framework import viewsets
from escola.models import Aluno, Curso
from serializer import AlunoSerializer, CursoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exisbindo todos os alunos"""
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exisbindo todos os cusros"""
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializer
