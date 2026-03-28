from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name=None),
    path('', views.home, name=None),
]