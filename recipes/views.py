from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
    return render(request, 'view.html', {
        'title': 'Home',
        'page': 'pages/home.html'
    }, None, 200, None)


def contact(request):
    return render(request, 'view.html', {
        'title': 'Contato',
        'page': 'pages/contact.html'
    }, None, 200, None)


def about(request):
    return render(request, 'view.html', {
        'title': 'Sobre',
        'page': 'pages/about.html'
    }, None, 200, None)
