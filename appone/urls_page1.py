from django.urls import path
from appone import views

urlpatterns = [
    path('',views.page1,name = 'page1'),
]