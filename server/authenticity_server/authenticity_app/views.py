from django.shortcuts import render
# authenticity_app/views.py
from rest_framework import generics
from .models import VideoAnalysis
from .serializers import VideoAnalysisSerializer

class VideoAnalysisListCreateView(generics.ListCreateAPIView):
    queryset = VideoAnalysis.objects.all()
    serializer_class = VideoAnalysisSerializer

class VideoAnalysisDetailView(generics.RetrieveAPIView):
    queryset = VideoAnalysis.objects.all()
    serializer_class = VideoAnalysisSerializer
