from django.db import models

# Create your models here.
class Enquete(models.Model):
    texto = models.CharField(max_length=200)
    data_publicacao = models.DateField()
    

