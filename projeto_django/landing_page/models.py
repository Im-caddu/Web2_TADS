from django.db import models

# Create your models here.
class Aluno ( models.Model ) :
    nome = models.CharField ( max_length =100)
    email = models.EmailField ()
    idade = models.IntegerField ()