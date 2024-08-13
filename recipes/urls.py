from django.contrib import admin
from django.urls import path
from recipes.views import home, contact, about, recipe

app_name = 'recipes'

urlpatterns = [
    path('', home, name='default'),
    path('home/', home, name='home'),
    path('index/', home, name='index'),
    path('contact/', contact),
    path('about/', about),
    path('<int:id>/', recipe, name='detail'),
    # path('category/<int:id>/', home)
]

