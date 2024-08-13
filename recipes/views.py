from django.shortcuts import render, redirect
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from .models import Recipe
import pdb

def home(request, id=None):
    data = Recipe.objects.filter(status=1).order_by('-id')
        
    return render(request, 'pages/home.html', {
        'title': 'Home',
        'page': 'pages/home.html',
        'data': data
    }, None, 200, None)


def contact(request):
    return render(request, 'pages/contact.html', {
        'title': 'Contato',
        'page': 'pages/contact.html'
    }, None, 200, None)


def about(request):
    return render(request, 'pages/about.html', {
        'title': 'Sobre',
        'page': 'pages/about.html'
    }, None, 200, None)
    

def recipe(request, id:int):    
    data = Recipe.objects.filter(id=id, status=1).first()
        
    if not data:
        return redirect('/')
            
    return render(request, 'pages/recipe.html', {
        'title': 'Receita',
        'page': 'pages/recipe.html',
        'item': data
    }, None, 200, None)
