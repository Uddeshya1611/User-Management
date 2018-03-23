from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('user_detail/', views.user_detail, name='user_detail'),
    path('account_login', views.account_login, name='account_login'),
    path('account_logout/', views.account_logout, name='account_logout'),
    path('account_signup/', views.account_signup, name='account_signup'),
]
