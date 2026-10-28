from django import forms
from .models import Post

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    correo = forms.EmailField(label="Correo electrónico")
    mensaje = forms.CharField(label="Mensaje",min_length=10, widget=forms.Textarea(attrs={"rows": 5}))

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "estado", "imagen"]

        labels = {
            "titulo": "Título del post",
            "contenido": "Contenido",
            "autor": "Autor",
            "estado": "Estado de publicación",
            "imagen": "Imagen del post"
        }
        widgets = {
            "titulo": forms.TextInput(attrs={
                "placeholder": "Escribe el título del post"
            }),
            "autor": forms.TextInput(attrs={
                "placeholder": "Escribe el nombre del autor"
            }),
            "contenido": forms.Textarea(attrs={
                "rows": 6,
                "placeholder": "Escribe el contenido del post"
            }),
        }

    def clean_titulo(self):

        titulo = self.cleaned_data.get("titulo")
        if len(titulo) < 5:
            raise forms.ValidationError("El título debe tener al menos 5 caracteres.")

        return titulo

class BuscarForm(forms.Form):
    q = forms.CharField(label="Buscar", required=False, widget=forms.TextInput(attrs={
        "placeholder": "Buscar posts por título"
    }))

