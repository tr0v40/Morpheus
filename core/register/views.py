from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

# Create your views here.
#Tipos de pacotes
def Listype(request):
    types = TypePack.objects.all()
    return render(request, 'listype.html', {'types': types})

def Newtype(request):
    form = TypForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Listype')
    return render(request, 'newtype.html', {'form': form})

def Uptype(request, id):
    types = get_object_or_404(TypePack, pk=id)
    form = TypForm(request.POST or None, instance=types)
    if form.is_valid():
        form.save()
        return redirect('Listype')
    return render(request, 'newtype.html', {'form':form})

def Deltype(request, id):
    types = get_object_or_404(TypePack, pk=id)
    if request.method == 'POST':
        types.delete()
        return redirect('Listype')
    return render(request, 'newtype.html', {'types':types})