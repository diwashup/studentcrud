from django.urls import path
from . import views 
from .views import list, create, update, delete

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
