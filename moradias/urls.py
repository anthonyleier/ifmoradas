from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('novo/', views.novo, name='novo'),
    # path('ver/<int:pk>/', views.ver, name='ver'),
    # path('editar/<int:pk>/', views.editar, name='editar'),
    # path('remover/<int:pk>/', views.remover, name='remover'),
    
    # path('create/', views.create, name='create'),
    # path('update/<int:pk>/', views.update, name='update'),
]