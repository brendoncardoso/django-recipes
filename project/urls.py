from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', include('recipes.urls')),
    path('', RedirectView.as_view(url='/recipes/', permanent=True)),
    path('home/', RedirectView.as_view(url='/recipes/', permanent=True)),
    path('index/', RedirectView.as_view(url='/recipes/', permanent=True))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)