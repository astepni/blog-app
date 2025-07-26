from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Tutaj możesz dodać kolejne ścieżki, np. do logowania, profilu itp.
]
