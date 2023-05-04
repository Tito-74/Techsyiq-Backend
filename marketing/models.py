from django.db import models

# Create your models here.
class Subscription(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=100, null=False, blank=False)
    terms_conditions = models.BooleanField(default=True)


class FiguresAnalysis(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    employed_alumin = models.CharField(max_length=10, null=False, blank=False)
    graduates = models.CharField(max_length=10, null=False, blank=False)
    commitment_percentage = models.CharField(max_length=4, null=False, blank=False)