from django import forms
from .models import Feedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Obrigatório. Digite um endereço de e-mail válido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['servico', 'tipo', 'descricao', 'anexo']
