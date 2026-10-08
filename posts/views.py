from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "posts/inicio.html")

# def lista_posts(request):
#     return HttpResponse("Lista de posts del blog")

def lista_posts(request):
    posts = [
        {"id": 1, "titulo": "Mi primer post", "autor": "Ana"},
        {"id": 2, "titulo": "Aprendiendo Django", "autor": "Luis"},
        {"id": 3, "titulo": "Rutas y vistas", "autor": "Marta"},
    ]
    
    return render(request, "posts/lista_posts.html", {"posts": posts})

def contacto(request):
    return HttpResponse("Página de contacto")

def detalle_post(request, post_id):
    post = {
        "id": post_id,
        "titulo": f"Post numero {post_id}",
        "contenido": "Contenido de ejemplo del post",
        "autor": "Autor del post",
    }
    return render(request, "posts/detalle_post.html", {"post": post})