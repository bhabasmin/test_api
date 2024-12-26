

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')

    def __str__(self):
        return self.client_name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='project')
    assigned_users = models.ManyToManyField(User, related_name='projects')

    def __str__(self):
        return self.project_name
