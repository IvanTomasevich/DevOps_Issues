from django.db import models
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
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


class Ticket(models.Model):
    title = models.CharField(max_length=48)
    sub_title = models.CharField(max_length=96)
    body = RichTextUploadingField()
    tipe = models.CharField(max_length=2, choices=tipe_incident)
    level = models.CharField(max_length=3, choices=level_choices, default='Mid')
    create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
