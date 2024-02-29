from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Tarefa, Usuario
from .forms import UsuarioForms

# Create your views here.

def listarUsuarios(request):
    
    if request.method == "GET" and request.GET.get("buscar"):
        usuario = Usuario.objects.filter(nome__contains=request.GET.get("buscar"))
        context = {"usuarios" : usuario}
    else:
        usuarios = Usuario.objects.all()
        context = {"usuarios" : usuarios}

    return render(request, "listarUsuarios.html", context)

def cadastroUsuario(request):
    
    if request.method == "POST":
        form = UsuarioForms(request.POST)

        if(form.is_valid()):
            usuario = Usuario()
            usuario.nome = form.cleaned_data["nome"]
            usuario.email = form.cleaned_data["email"]
            usuario.save()
            
            return HttpResponseRedirect("tarefas/listarUsuarios")
    else:
        formUsuario  = UsuarioForms()
    
    return render(request, "formUsuario.html", {"form": formUsuario})

def excluirUsuario(request, id):
    
    if request.method == "GET":
        usuario = Usuario.objects.get(pk=id)
        usuario.delete()
        
        return HttpResponseRedirect("tarefas/listarUsuarios")
    
def editarUsuario(request, id):
    
    if request.method == "GET":
        usuario = Usuario.objects.get(pk=id)
        context = {"usuario" : usuario}
        return render(request, "formEditarUsuario.html", context)
    
    if request.method == "POST":
        form = UsuarioForms(request.POST)
        
        if form.is_valid():
            usuario = Usuario.objects.get(pk=id)
            usuario.nome = form.cleaned_data['nome']
            usuario.email = form.cleaned_data['email']
            usuario.save()
            
            return HttpResponseRedirect("/tarefas/listarUsuarios")