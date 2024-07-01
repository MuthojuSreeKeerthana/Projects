from django.http import HttpResponse
from django.shortcuts import render

app_name='mp'

def home(request):
    return render(request , 'index.html')