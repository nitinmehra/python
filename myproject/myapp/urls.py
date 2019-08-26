from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about_us'),
    path('enrollment-form', views.enrollment_page, name='enrollment_page'),
    path('enrollment_from_submit', views.enrollment_from_submit, name='enrollment_from_submit'),
]