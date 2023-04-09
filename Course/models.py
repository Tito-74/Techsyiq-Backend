from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    period = models.CharField(max_length=50, null=False, blank=False)