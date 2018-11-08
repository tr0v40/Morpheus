from django.shortcuts import render

#Index

def Index(request):
    return render(request, 'index.html')
