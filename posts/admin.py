from django.contrib import admin
from .models import Post

admin.site.site_header = "Administración de Mi Blog"
admin.site.site_title = "Panel del Blog"
admin.site.index_title = "Gestión de contenidos"

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_creacion", "estado")
    list_filter = ("estado", "fecha_creacion")
    search_fields = ("titulo", "contenido", "autor")
    list_editable = ("estado",)
    ordering = ("-fecha_creacion",)
    list_per_page = 10

admin.site.register(Post, PostAdmin)