from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Testimonial(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, default=None)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='created_at')
    description = models.TextField(default=None, null=False, blank=False)
    linkedin_link = models.URLField(max_length = 200, null=True, blank=True)
    title = models.CharField(max_length=150, null=False, blank=False)
    image = CloudinaryField('images',default = None)
    logo = models.CharField(max_length=150, null=False, blank=False)


    def __str__(self):
        return self.name