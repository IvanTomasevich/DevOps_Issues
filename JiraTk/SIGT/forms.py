from django import forms
from .models import Ticket
from ckeditor_uploader.widgets import *


class CreateTicket(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Ticket
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtiene el usuario pasado como argumento
        super().__init__(*args, **kwargs)
        if user:
            self.instance.user = user  # Asigna el usuario a la instancia del modelo
