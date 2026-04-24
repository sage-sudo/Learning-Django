from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name=None),
    path('', views.main, name=None),
    path('members/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
]