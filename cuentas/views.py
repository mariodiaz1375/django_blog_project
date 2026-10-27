from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import RegistroForm

# Create your views here.
def registro(request):
    if request.user.is_authenticated:
        return redirect("lista_posts")

    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect("lista_posts")
    else:
        form = RegistroForm()
    return render(request, "cuentas/registro.html", {"form": form})