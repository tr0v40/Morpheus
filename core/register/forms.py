from django.forms import ModelForm
from .models import *

class TypForm(ModelForm):
    class Meta:
        model = TypePack
        fields = ['package', 'weight']