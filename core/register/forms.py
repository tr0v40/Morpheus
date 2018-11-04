from django.forms import ModelForm, ModelChoiceField
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

#Clientes

class ClientForm(ModelForm):
    class Meta:
        model = RegCli
        fields = ['com_name', 'adress', 'state', 'country', 'contact']

