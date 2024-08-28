from django.db import models
from django.contrib.auth.models import User


class Annotator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    count = models.IntegerField(default=0)


class DataAnnotation(models.Model):
    annotator = models.ForeignKey(Annotator, on_delete=models.CASCADE)
    first_name_en = models.CharField(max_length=100, blank=True, null=True)
    middle_name_en = models.CharField(max_length=100, blank=True, null=True)
    last_name_en = models.CharField(max_length=100, blank=True, null=True)
    first_name_bn = models.CharField(max_length=100, blank=True, null=True)
    middle_name_bn = models.CharField(max_length=100, blank=True, null=True)
    last_name_bn = models.CharField(max_length=100, blank=True, null=True)
    audio = models.FileField(upload_to='audio', max_length=100, blank=True, null=True)
