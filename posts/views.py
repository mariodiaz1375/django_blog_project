from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

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
    contacto = {
        "email": "contacto_mdiaz@miblog.com",
        "twitter": "@mdiaz",
    }
    return render(request, "posts/contacto.html", {"contacto": contacto})

def detalle_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return HttpResponse("El post no existe.")
    
    return render(request, "posts/detalle_post.html", {"post": post})


