from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    context = {
        'title': 'this is the title', 
        'header1': 'this is header one',
        }
    return render(request, 'homepage/index.html', context  )