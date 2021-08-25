from django.urls import path

from . import views

app_name = 'Tedx'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('services/', views.services),
    path('contactUs/', views.contactUs),
    path('about/', views.about),


]