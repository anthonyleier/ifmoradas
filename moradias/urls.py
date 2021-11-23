from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo/', views.novo, name='novo'),
    path('detalhes/<int:pk>/', views.detalhes, name='detalhes'),
    path('editar/<int:pk>/', views.editar, name='editar'),
    path('remover/<int:pk>/', views.remover, name='remover'),

    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),

    path('erro/', views.erro, name='erro'),

    path('telaLogin', views.telaLogin, name='telaLogin'),
    path('telaRegistro', views.telaRegistro, name='telaRegistro'),
    path('registrar', views.registrar, name='registrar'),
    path('logar', views.logar, name='logar'),
    path('logout', views.deslogar, name='logout'),

    path('telaImagem', views.telaImagem, name='telaImagem'),
    path('novaImagem', views.novaImagem, name="novaImagem")

]
