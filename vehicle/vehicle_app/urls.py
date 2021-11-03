from django.urls import path
from . import views

urlpatterns = [
    path('', views.Vehicle.index, name='index'),
    path('add/', views.Vehicle.add, name='add'),
    path('status/<uuid:id>/', views.Vehicle.status, name='status'),
    path('update/<uuid:id>/', views.Vehicle.update, name='update'),
    path('delete/<uuid:id>/', views.Vehicle.delete, name='delete'),
]
