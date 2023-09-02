from home import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('courses', views.course, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('search', views.search, name='search')

]
