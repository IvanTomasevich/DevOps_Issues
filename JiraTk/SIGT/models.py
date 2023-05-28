from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
# Choices para IssueTicket
tipe_incident = [
    ("IN", "Incident"),
    ("RQ", "Request"),
]

level_choices = [
    ("Low", "Bajo"),
    ("Mid", "Medio"),
    ("Hi", "Alta"),
    ("VHI", "Critico"),
]


class IssueTicket(models.Model):
    title = models.CharField(max_length=48)
    sub_title = models.CharField(max_length=96)
    body = RichTextField(max_length=512)
    create = models.DateTimeField(auto_now_add=True)
