from datetime import datetime

from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import CASCADE
from rest_framework import serializers


class Todo(models.Model):
    description    = models.CharField(max_length=500)
    targetDate    = models.DateField(default=timezone.now)
    IsDone         = models.BooleanField()
    user = models.ForeignKey("auth.User", db_column="user",on_delete=CASCADE)


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'