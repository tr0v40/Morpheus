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

#Produtos
def LisProd(request):
    prods = Prod.objects.all()
    return render(request, 'lisprod.html', {'prods': prods})

def NewProd(request):
    form = ProdForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('LisProduct')
    return render(request, 'newprod.html', {'form': form})

def UpProd(request, id):
    prods = get_object_or_404(Prod, pk=id)
    form = ProdForm(request.POST or None, instance=prods)
    if form.is_valid():
        form.save()
        return redirect('LisProduct')
    return render(request, 'newprod.html', {'form':form})

def DelProd(request, id):
    product = get_object_or_404(Prod, pk=id)
    if request.method == 'POST':
        product.delete()
        return redirect('LisProduct')
    return render(request, 'newprod.html', {'product':product})

#Clientes
def LisCli(request):
    clients = RegCli.objects.all()
    return render(request, 'liscli.html', {'clients': clients})

def NewCli(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('LisClient')
    return render(request, 'newcli.html', {'form': form})

def UpCli(request, id):
    clients = get_object_or_404(RegCli, pk=id)
    form = ClientForm(request.POST or None, instance=clients)
    if form.is_valid():
        form.save()
        return redirect('LisClient')
    return render(request, 'newcli.html', {'form':form})

def DelCli(request, id):
    clients = get_object_or_404(RegCli, pk=id)
    if request.method == 'POST':
        clients.delete()
        return redirect('LisClient')
    return render(request, 'index.html', {'clients':clients})