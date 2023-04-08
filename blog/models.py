from django.db import models
from django.conf import settings
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255, blank = False)
  
  def __str__(self):
    return self.name
  

class Blog(models.Model):
  title = models.CharField(max_length=255, blank = False)
  description = RichTextField(null=False, blank=False)
  image = CloudinaryField('images', default=None)
  date_published = models.DateTimeField(auto_now_add=True,verbose_name='date_published')
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

  def __str__(self):
    return self.title