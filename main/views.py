from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
# Create your views here.

def main(request):
    context = {'block content':'<h1>This is main page. Now it\'s shitty but I will change it soon<h2>'}
    return render(request, 'main/index.html', context)