from django.urls import path
from django.conf.urls.static import static
from .views import handler

urlpatterns = [
    path('', handler, name='homepage'),
    ]