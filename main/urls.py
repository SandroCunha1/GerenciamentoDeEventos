from django.urls import path

from . import views

urlpatterns = [   
    path('<int:id>', views.list, name='list'),
    path('evento-list/', views.evento_list, name='evento_list'),
    path('evento-form/', views.evento_create, name='evento-form'),
    path('view/', views.view, name='view'),
    path('', views.home, name='home'),
]
