from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('user_enrollment', views.user_enrollment, name='user_enrollment'),
    path('enrollment_from_submit', views.enrollment_from_submit, name='enrollment_from_submit'),
    path('users_list', views.users_list, name='users_list'),
    path('user_login', views.user_login, name='user_login'),
]