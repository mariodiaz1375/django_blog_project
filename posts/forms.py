from django import forms
from .models import Post

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    correo = forms.EmailField(label="Correo electrónico")
    mensaje = forms.CharField(label="Mensaje",min_length=10, widget=forms.Textarea(attrs={"rows": 5}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "autor", "estado"]

        labels = {
            "titulo": "Título del post",
            "contenido": "Contenido",
            "estado": "Estado de publicación",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={
                "placeholder": "Escribe el título del post"
            }),
            "contenido": forms.Textarea(attrs={
                "rows": 6,
                "placeholder": "Escribe el contenido del post"
            }),
        }

