from django.contrib import admin
from django.db import router
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register( 'alunos', AlunosViewSet, basename='Alunos' )
router.register( 'cursos', CursosViewSet, basename='Cursos' )
router.register( 'matriculas', MatriculasViewSet, basename='Matrículas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]
