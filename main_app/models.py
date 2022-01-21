from django.db import models

# Create your models here.
class Widget(models.Model):
  widget = models.CharField(max_length=50)

  def __str__(self):
    return self.item