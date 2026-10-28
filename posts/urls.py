from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("posts/", views.lista_posts, name="lista_posts"),
    path("contacto/", views.contacto, name="contacto"),
    path("crear_post/", views.crear_post, name="crear_post"),
    path("mis_posts/", views.mis_posts, name="mis_posts"),
    path("posts/<slug:slug>/", views.detalle_post, name="detalle_post"),
    # path("posts/<int:post_id>/", views.detalle_post, name="detalle_post"),
    path("posts/<slug:slug>/editar/", views.editar_post, name="editar_post"),
    path("posts/<slug:slug>/eliminar/", views.eliminar_post, name="eliminar_post"),
]