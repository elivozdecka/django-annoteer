from random import choices

from django.db import models
from django import forms
from django.contrib.auth.models import User


class Annotation(models.Model):
    STATUS_CHOICES = [
        (1, "Unannotated"),
        (2, "Annotated"),
        (3, "Finished Annotation")
    ]
    text =models.TextField(blank=False) #in stead of text, just buttons "Yes" or "No"
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, default=1)
    finished_annotation =forms.ChoiceField(choices=("Ja", "Nein"))
    annotated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    last_modified_at = models.DateTimeField(auto_now=True)
    saved = models.BooleanField(default=False)
    last_saved = models.DateTimeField(auto_now=True)


# Create your models here.
