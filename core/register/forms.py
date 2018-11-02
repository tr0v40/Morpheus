from django.forms import ModelForm
from .models import *

#Embalagens
class TypForm(ModelForm):
    class Meta:
        model = TypePack
        fields = ['package', 'weight']

#Produtos
class ProdForm(ModelForm):
    class Meta:
        model = Prod
        fields = ['product', 'ncm']