from django.db import models

# Create your models here.
class details(models.Model):
    name = models.CharField(max_length=400)
    email = models.EmailField(max_length=400)
    def __str__(self):
        return self.name