from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('ob/', views.index, name='index'),
    path('cats/<int:catid>/', views.category, name='cats'),
    path('post/<int:pk>/', views.post_info, name='post_info'),
]