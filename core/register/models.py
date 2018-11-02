from django.db import models

# Create your models here.

class TypePack(models.Model):
    id = models.AutoField(primary_key=True)
    package = models.CharField(max_length=100)
    weight =models.DecimalField(decimal_places=2, max_digits=5)

    def __str__(self):
        return self.package
