from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def currentBlog(request):
    return HttpResponse('Current blog')
