from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about_us'),
    path('enrollment-form', views.enrollment_page, name='enrollment_page'),
]