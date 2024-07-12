from django.contrib import admin
from django.urls import path
from recipes.views import home, contact, about, recipe


urlpatterns = [
    path('', home),
    path('home/', home),
    path('index/', home),
    path('contact/', contact),
    path('about/', about),
    path('<uuid:id>/', recipe)
]

