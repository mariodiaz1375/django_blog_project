from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    correo = forms.EmailField(label="Correo electrónico")
    mensaje = forms.CharField(label="Mensaje",min_length=10, widget=forms.Textarea(attrs={"rows": 5}))