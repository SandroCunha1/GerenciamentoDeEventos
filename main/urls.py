from django.urls import path

from . import views

urlpatterns = [   
    path('<int:id>', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('view/', views.view, name='view'),
    path('', views.home, name='home'),
]
