from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, PerfilForm
from .models import Perfil

# Create your views here.
def registro(request):
    if request.user.is_authenticated:
        return redirect("lista_posts")

    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Perfil.objects.create(user=user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect("lista_posts")
    else:
        form = RegistroForm()
    return render(request, "cuentas/registro.html", {"form": form})

@login_required
def mi_perfil(request):
    return render(request, "cuentas/perfil_usuario.html")

@login_required
def editar_perfil(request):
    perfil = request.user.perfil

    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if form.is_valid():
            form.save()
            return redirect("lista_posts")

    else:
        form = PerfilForm(instance=perfil)

    return render(request, "cuentas/editar_perfil.html", {"form": form})