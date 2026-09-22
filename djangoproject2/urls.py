from django.contrib import admin
from django.urls import include, path

from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('properties/', include('properties.urls')),
    path('', home, name='home'),
]
