from django.db import models

# Create your models here.
STARTING_DATE = (
    ("2ND Feb","2ND Feb"),
    ("8th Aug", "8th Aug"),
    ("9th Nov", "9th Nov"),
  )
# application model
class Application(models.Model):
  name = models.CharField(max_length=255, null = False, blank = False)
  phone_no = models.CharField(max_length=255, null = False, blank = False)
  email = models.EmailField(max_length=255, null = False, blank = False)
  module = models.CharField(max_length=255, null = False, blank = False)
  starting_date = models.CharField(max_length=255, choices = STARTING_DATE,
  default = '2ND Feb', null=False)

  def __str__(self): 
    return self.name