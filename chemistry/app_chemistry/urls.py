from django.urls import path

from app_chemistry.views import homepage


urlpatterns = [
    path('', homepage, name='homepage'),
]