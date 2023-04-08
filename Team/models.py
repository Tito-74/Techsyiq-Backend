from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField

# Create your models here.
class Team(models.Model):
  name = models.CharField(max_length=255)
  title= models.CharField(max_length=255)
  social_media_link = models.URLField(blank=True)
  description = models.TextField(blank=False)
  image = CloudinaryField('images', default=None)
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  def __str__(self):
    return self.name