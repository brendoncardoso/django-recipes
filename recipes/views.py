from django.shortcuts import render, redirect
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
import pdb

def home(request):
    data = [make_recipe() for _ in range(10)]
        
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
    

def recipe(request, id:str):    
    item = make_recipe()
        
    # if 'id' in data and data.get('id') != id:
    #     return redirect('/')
    
    # pdb.set_trace()
    
    return render(request, 'pages/recipe.html', {
        'title': 'Receita',
        'page': 'pages/recipe.html',
        'item': item
    }, None, 200, None)

