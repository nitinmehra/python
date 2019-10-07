from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us', views.about_us, name='about_us'),
    path('user_enrollment', views.user_enrollment, name='user_enrollment'),
    path('users_list', views.users_list, name='users_list'),
    path('user_login', views.user_login, name='user_login'),
    path('logout', views.logout, name='logout'),
    path('user_edit/<int:id>', views.user_edit, name='user_edit'),
    #path('user_update/<int:id>', views.user_update, name='user_update'),
]