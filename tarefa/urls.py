from django.urls import path
from .views import listarUsuarios, cadastroUsuario, excluirUsuario, editarUsuario

urlpatterns = [
    path("listarUsuarios", listarUsuarios),
    path("cadastroUsuario", cadastroUsuario),
    path("excluirUsuario <int:id>", excluirUsuario),
    path("editarUsuario <int:id>", editarUsuario),
]
