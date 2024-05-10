"""
URL configuration for feedback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from IT_COURSE import views
import IT_COURSE
urlpatterns = [
    path('',views.home,name='Home'),
    path('admin/',admin.site.urls),
    path('AboutUs/',views.AboutUs,name='AboutUs'),
    path('ContactUs/',views.ContactUs,name='ContactUs'),
    path('CoursesOffered/',views.CoursesOffered,name='CoursesOffered'),
    path('home/SignUp/',views.SignUp,name='SignUp'),
    path('feedback/',views.feedback,name='feedback'),
    path('reviews/',views.showfeedback, name='reviews'),
    path('home/SignIn/',views.SignIn, name='SignIn'),
    path('SignOut/',views.SignOut, name='SignOut'),
    path('Models/',views.Models,name='Models'),
    path('RI/',views.RI,name='RI'),
    path('Freshers/',views.Freshers,name='Freshers'),
    path('full_stack_python/',views.fullstackpython,name='full_stack_python'),
    path('full_stack_java/', views.fullstackjava, name='full_stack_java'),
    path('mern_stack/', views.mernstack, name='mern_stack'),
    path('data_analytics/', views.dataanalytics, name='data_analytics'),
    path('devops/', views.devops, name='devops'),
    path('aws/',views.aws, name="aws"),
    path('Msg/', views.Msg, name='Msg'),
    #path('payment/',views.payment, name='payment'),
    #path('success/',views.success, name='success'),
]