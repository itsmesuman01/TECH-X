# users/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('add/', views.add_user, name='add_user'),
    path('update/<int:id>/', views.update_user, name='update_user'),
    path('delete/<int:id>/', views.delete_user, name='delete_user'),
]
