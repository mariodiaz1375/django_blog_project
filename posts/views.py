from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Post
from .forms import ContactoForm, PostForm

# Create your views here.
def inicio(request):
    return render(request, "posts/inicio.html")

# def lista_posts(request):
#     return HttpResponse("Lista de posts del blog")

def lista_posts(request):
    posts = Post.objects.filter(estado='publicado').order_by("-fecha_creacion")

    context = {
        "posts": posts,
    }   
    
    return render(request, "posts/lista_posts.html", context)

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            correo = form.cleaned_data["correo"]   
            mensaje = form.cleaned_data["mensaje"]

            print("Nombre:", nombre)
            print("Correo:", correo)
            print("Mensaje:", mensaje)

            return HttpResponse(f"¡Gracias por contactarnos, {nombre}!")
    else:
        form = ContactoForm()
    return render(request, "posts/contacto.html", {"form": form})

def detalle_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponse("El post no existe.")
    
    return render(request, "posts/detalle_post.html", {"post": post})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("lista_posts")
    else:
        form = PostForm()

    return render(request, "posts/crear_post.html", {"form": form})







