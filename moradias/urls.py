from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('novo/', views.novo, name='novo'),
    # path('create/', views.create, name='create'),
    # path('editar/', views.editar, name='editar'),
    # path('update/<int:pk>/', views.update, name='update'),
    # path('remover/<int:pk>/', views.remover, name='remover'),
]