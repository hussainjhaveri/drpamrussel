from django.urls import path

from . import views

app_name = 'tBT'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('services/', views.services, name='services'),
    path('contactUs/', views.contactUs.as_view(), name='contactUs'),
    path('about/', views.about, name='about'),
    path('mockindex/', views.mockindex, name='mockindex'),
    path('aboutmock/', views.aboutmock, name='aboutmock'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('faq/', views.faq, name='faq'),
    path('newsreports/', views.newsreports, name='newsreports'),

]