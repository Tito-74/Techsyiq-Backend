from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, default=None,)
    description = models.TextField(default=None, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='created_at')
    period = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name