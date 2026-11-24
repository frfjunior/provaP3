from django.urls import path
from . import views

urlpatterns = [
    path("lotes/", views.lista_lotes, name="lista_lotes"),
    path("lotes/novo/", views.novo_lote, name="novo_lote"),
    path("lotes/<int:id>/", views.detalhe_lote, name="detalhe"),
]