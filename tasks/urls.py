from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>/', views.update, name='update'), #using <int:pk> makes it dynamic.
    path('delete/<int:pk>/', views.delete, name='delete')
]
