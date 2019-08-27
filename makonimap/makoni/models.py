from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Entidades que representam o modelo de negocio do makoni-map

class Endereco(models.Model):
    rua = models.CharField(max_length=30)
    cep = models.CharField(max_length=30)
    cidade = models.CharField(max_length=20)
    state = (
        ('PE','Pernambuco'),
        ('PB','Paraíba'),
        ('CE','Ceará'),
        ('SP','São Paulo'),
        ('SE','SERGIPE'),
        ('RJ', 'Rio de Janeiro'),
        ('RS','Rio Grande do Sul'),
        ('RN', 'Rio Grande do Norte'),
        ('AC','Acre'),
        ('AL','Alagoas'),
        ('AP','Amapá'),
        ('AM','Amazonas'),
        ('BA','Bahia'),
        ('DF','Distrito Federal'),
        ('ES','Espirito Santo'),
        ('GO','Goiás'),
        ('MA','Maranhão'),
        ('MT','Mato Grosso'),
        ('MS','Mato Grosso do Sul'),
        ('MG','Minas Gerais'),
        ('PA','Pará'),
        ('PR','Paraná'),
        ('PI','Piaui'),
        ('RO','Rondônia'),
        ('RR','Roraima'),
        ('SC','Santa Catarina'),
        ('TO','Tocantins')
    )
    estado = models.CharField(max_length=25,choices=state)  

    def __str__(self):
        return self.rua

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    idade = models.CharField(max_length=10)
    endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE)
    user = models.OneToOneField(User,related_name="user",on_delete=models.CASCADE)    

    def __str__(self):
        return self.name


class Photo(models.Model):
    description = models.CharField(max_length=500,default=None,null=True)
    reference_point = models.CharField(max_length=300,default=None,null=True)
    url_photo = models.CharField(max_length=1000,default=None,null=True)
    def __str__(self):
        return self.reference_point


class Localization(models.Model):
    latitude= models.FloatField(null=True,default=None)
    longitude = models.FloatField(null=True,default=None)
    description = models.CharField(max_length=500,default=None,null=True)
    endereco = models.ForeignKey(Endereco,on_delete=models.CASCADE)
    photos= models.ManyToManyField(Photo,verbose_name='list of photos')

    def __str__(self):
        return self.endereco


class Router(models.Model):
    router = models.CharField(max_length=30,default=None)
    localization = models.ForeignKey(Localization,on_delete=models.CASCADE)
    user_point_origen = models.ForeignKey(Person,on_delete=models.CASCADE)

    def __str__(self):
        return self.router

