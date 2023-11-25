# authenticity_app/urls.py
from django.urls import path
from .views import VideoAnalysisListCreateView, VideoAnalysisDetailView

urlpatterns = [
    path('analyses/', VideoAnalysisListCreateView.as_view(), name='analysis-list'),
    path('analyses/<int:pk>/', VideoAnalysisDetailView.as_view(), name='analysis-detail'),
]
