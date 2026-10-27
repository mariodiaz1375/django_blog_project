from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

user = get_user_model()

class RegistroForm(UserCreationForm):

    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta(UserCreationForm.Meta):
        model = user
        fields = ("username", "email")

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        if user.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("El correo electrónico ya está registrado.")
        return email