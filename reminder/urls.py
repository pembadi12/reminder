from django.urls import path
from . import views

urlpatterns=[
    path('', views.event_list, name='event_list'),
    path('add/', views.add_event, name='add_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path('edit/<int:event_id>/', views.event_edit, name='event_edit'), 
    ]