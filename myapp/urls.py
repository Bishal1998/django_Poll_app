from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'), 
    path('result/<int:id>', views.result, name='result'),
    path('vote/<int:id>', views.vote, name='vote'),

]