from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='test1-home'),
    path('about/', views.about, name='test1-about'),
]