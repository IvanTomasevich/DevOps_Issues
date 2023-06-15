from django import forms
from .models import Ticket
from ckeditor_uploader.widgets import *


class CreateTicket(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Ticket
        fields = '__all__'
        widgets = {
            fields: forms.TextInput(attrs={'class': 'form-floating'})
        }

