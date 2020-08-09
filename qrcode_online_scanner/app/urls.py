from app import views
from django.urls import path

urlpatterns = [
    path('scanner/', views.scanner),
]