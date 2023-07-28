from core import views
from django.urls import path

app_name = 'core'

urlpatterns = [
    path('view_attestation/', views.attestation_view, name='view_attestation'),
]