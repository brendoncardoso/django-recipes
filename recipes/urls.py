from django.contrib import admin
from django.urls import path
from recipes.views import home, contact, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home', home),
    path('index', home),
    path('contact/', contact),
    path('about/', about),
]

