from django.urls import path
from . import views

urlpatterns = [
    path('process/', views.process_text, name='process_text'),
    path('get_processed_text/', views.get_processed_text, name='get_processed_text'),
]


