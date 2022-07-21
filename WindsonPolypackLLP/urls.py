from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pp-woven-fabrics/', views.ppWovenFabrics, name='pp-woven-fabrics'),
    path('pp-woven-bags/', views.ppWovenBags, name='pp-woven-bags'),
    path('contact/', views.contact, name='contact'),
]
