from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name=None),
    path('members/', views.members, name=None),
    path('details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]