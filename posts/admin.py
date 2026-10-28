from django.contrib import admin
from .models import Post

admin.site.site_header = "Administración de Mi Blog"
admin.site.site_title = "Panel del Blog"
admin.site.index_title = "Gestión de contenidos"

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_creacion", "estado", "slug")
    list_filter = ("estado", "fecha_creacion")
    search_fields = ("titulo", "contenido", "autor__username")
    list_editable = ("estado",)
    ordering = ("-fecha_creacion",)
    list_per_page = 10
    prepopulated_fields = {"slug": ("titulo",)}  # genera el slug a partir del titulo del post

admin.site.register(Post, PostAdmin)