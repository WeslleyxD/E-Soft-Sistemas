from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar, name='cadastrar'),
    path('listar_cadastros/', views.listar_cadastros, name='listar_cadastros'),
    path('editar_cadastro/<int:usuario_id>', views.editar_cadastro, name='editar_cadastro'),
    path('excluir_cadastro/<int:usuario_id>', views.excluir_cadastro, name='excluir_cadastro'),
]