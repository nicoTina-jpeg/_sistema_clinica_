# São as importações realizadas de forma a utilizar partes do django.
from django.urls import path
# Importação do módulo views.py, onde tem a view index
from sistema import views



# Lista responsável por organizar as urls do sistema.
urlpatterns = [
    path('seunome/', views.nome),
]