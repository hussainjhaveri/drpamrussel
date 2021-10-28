from django.urls import path

from . import views

app_name = 'tBT'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('services/', views.services, name='services'),
    path('contactUs/', views.contactUs.as_view(), name='contactUs'),
    path('about/', views.about, name='about'),
    path('ugh/', views.ugh, name='ugh'),
    path('assessments/', views.assessments, name='assessments'),


]