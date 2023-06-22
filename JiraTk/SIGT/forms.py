from django import forms
from .models import Ticket
from ckeditor_uploader.widgets import *
from django.contrib.auth.models import User


class CreateTicket(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Ticket
        fields = '__all__'
        exclude = ['author']
