from django.db import models


# Create your models here.
#tipos de embalagem
class TypePack(models.Model):
    id = models.AutoField(primary_key=True)
    package = models.CharField(max_length=100)
    weight =models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.package

#Produtos
class Prod(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100)
    ncm =models.CharField(max_length=100)

    def __str__(self):
        return self.product



#Clientes
class RegCli(models.Model):
    id = models.AutoField(primary_key=True)
    com_name = models.CharField(max_length=100, default="")
    adress = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=70, blank=True, null=True)
    country = models.CharField(max_length=70, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.com_name

#Telefones
