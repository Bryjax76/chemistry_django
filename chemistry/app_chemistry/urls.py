from django.urls import path

from app_chemistry.views import homepage, canvas


urlpatterns = [
    path('', homepage, name='homepage'),
    path('canvas.html', canvas, name='canvas'),
]