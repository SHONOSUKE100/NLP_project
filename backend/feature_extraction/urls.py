from django.urls import path
from . import views

urlpatterns = [
    path('process_with_rulebase/', views.process_with_rulebase_text, name='process_with_rulebase_text'),
    path('processed_with_rulebase/', views.get_processed_with_rulebase_text, name='get_processed_with_rulebase_text'),
    path('process_with_crf/', views.process_with_crf_text, name='process_with_crf_text'),
    path('processed_with_crf/', views.get_processed_with_crf_text, name='get_processed_with_crf_text'),
]




