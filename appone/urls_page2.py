from django.urls import path
from appone import views

urlpatterns = [
    path('',views.page2,name= 'page2'),
]