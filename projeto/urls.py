from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')),
    path('', RedirectView.as_view(url='/recipes/', permanent=True)),
    path('home/', RedirectView.as_view(url='/recipes/', permanent=True)),
    path('index/', RedirectView.as_view(url='/recipes/', permanent=True))
]
