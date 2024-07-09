from django.urls import path

from . import views

urlpatterns = [   
    path('<int:id>', views.list, name='list'),
    path('evento-list/', views.evento_list, name='evento_list'),
    path('evento-form/', views.evento_create, name='evento-form'),
    path('atracao-list/', views.atracao_list, name='atracao_list'),
    path('atracao-form/', views.atracao_create, name='atracao-form'),
    path('local-list/', views.local_list, name='local-list'),
    path('local-form/', views.create_local, name='create-local'),
    path('view/', views.view, name='view'),
    path('evento/<int:id>/', views.evento_detail, name='evento-detail'),
    path('', views.home, name='home'),
]
