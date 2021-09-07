from django.urls import path

from . import views

app_name = 'tBT'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('services/', views.services),
    path('contactUs/', views.contactUs),
    path('about/', views.about),
    path('ugh/', views.ugh),


]