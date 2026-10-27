from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
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

def detalle_post(request, slug):  # en caso de volver a usar el id del post, cambiar slug por post_id
    # try:
    #     post = Post.objects.get(id=post_id)
    # except Post.DoesNotExist:
    #     return HttpResponse("El post no existe.")

    post = get_object_or_404(Post, slug=slug)
    
    return render(request, "posts/detalle_post.html", {"post": post})


@login_required
def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # Agregar request.FILES para manejar la imagen

        if form.is_valid():
            
            form.save()
            return redirect("lista_posts")
    else:
        form = PostForm()

    return render(request, "posts/post_form.html", {
        "form": form,
        "texto_boton": "Crear post",
        "titulo_pagina": "Crear post"
    })

@login_required
def editar_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            
            form.save()
            return redirect("detalle_post", slug=post.slug)
        
    else:
        form = PostForm(instance=post)

    return render(request, "posts/post_form.html", {
        "form": form,
        "post": post,
        "titulo_pagina": "Editar post",
        "texto_boton": "Guardar cambios"
    })

@login_required
def eliminar_post(request, slug):

    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('lista_posts')

    return render(request, 'posts/confirm_delete_post.html', {'post': post})